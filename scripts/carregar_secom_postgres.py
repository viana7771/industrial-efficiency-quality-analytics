from __future__ import annotations

import argparse
import os
import re
from io import StringIO
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FEATURES = {
    "feature_021": 21,
    "feature_159": 159,
    "feature_161": 161,
    "feature_023": 23,
    "feature_062": 62,
    "feature_142": 142,
}
LABEL_PATTERN = re.compile(r'^\s*(-?\d+)\s+"([^"]+)"\s*$')


def preparar_dados() -> pd.DataFrame:
    raw = ROOT / "data" / "raw"
    dados = pd.read_csv(
        raw / "secom.data",
        sep=r"\s+",
        header=None,
        na_values="NaN",
        engine="python",
    )

    rotulos = []
    for numero_linha, linha in enumerate(
        (raw / "secom_labels.data").read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        match = LABEL_PATTERN.fullmatch(linha)
        if match is None:
            raise ValueError(f"Formato inválido em secom_labels.data, linha {numero_linha}.")
        rotulos.append(int(match.group(1)))

    if len(dados) != len(rotulos):
        raise ValueError("A quantidade de medições não corresponde à quantidade de rótulos.")
    if not set(rotulos).issubset({-1, 1}):
        raise ValueError("Foram encontrados rótulos diferentes de -1 e 1.")

    percentual_missing = dados.isna().mean()
    constantes = dados.columns[dados.nunique(dropna=True) <= 1]
    excesso_missing = percentual_missing[percentual_missing > 0.50].index
    tratados = dados.drop(columns=constantes.union(excesso_missing))
    tratados = tratados.fillna(tratados.median(numeric_only=True))

    ausentes = set(FEATURES.values()) - set(tratados.columns)
    if ausentes:
        raise ValueError(f"Features selecionadas removidas durante o tratamento: {sorted(ausentes)}")

    exportacao = tratados.loc[:, list(FEATURES.values())].copy()
    exportacao.columns = list(FEATURES)
    exportacao.insert(0, "falha", [int(rotulo == 1) for rotulo in rotulos])

    if exportacao.isna().any().any():
        raise ValueError("A seleção contém valores ausentes após o tratamento.")
    return exportacao


def main() -> None:
    parser = argparse.ArgumentParser(description="Carrega a seleção SECOM no PostgreSQL.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Valida e resume os dados sem conectar ao PostgreSQL.",
    )
    argumentos = parser.parse_args()

    dados = preparar_dados()
    print(f"Linhas preparadas: {len(dados)}")
    print(f"Features selecionadas para carga: {len(dados.columns) - 1}")
    print("Contagem por falha:")
    print(dados["falha"].value_counts().sort_index().to_string())
    print("Médias por grupo:")
    print(dados.groupby("falha").mean(numeric_only=True).to_string())
    if argumentos.dry_run:
        print("Dry-run concluído; nenhuma conexão foi aberta.")
        return

    database_url = os.environ.get("SECOM_DATABASE_URL")
    if not database_url:
        raise SystemExit(
            "Dados validados localmente. Para carregar no PostgreSQL, defina SECOM_DATABASE_URL."
        )

    import psycopg

    schema = (ROOT / "sql" / "01_secom_estrutura.sql").read_text(encoding="utf-8")
    colunas = ["falha", *FEATURES]
    tabela = ", ".join(colunas)
    csv_dados = StringIO()
    dados.to_csv(csv_dados, index=False, header=False)

    with psycopg.connect(database_url) as conexao:
        conexao.execute(schema, prepare=False)
        conexao.execute("TRUNCATE TABLE public.secom_tratado RESTART IDENTITY")
        with conexao.cursor() as cursor:
            with cursor.copy(
                f"COPY public.secom_tratado ({tabela}) FROM STDIN WITH (FORMAT CSV)"
            ) as copia:
                copia.write(csv_dados.getvalue())

            cursor.execute(
                "SELECT falha, total_observacoes, media_feature_021, "
                "media_feature_159, media_feature_161 "
                "FROM public.vw_secom_indicadores_top3 ORDER BY falha"
            )
            indicadores = cursor.fetchall()

            cursor.execute("SELECT COUNT(*) FROM public.secom_tratado")
            total_carregado = cursor.fetchone()[0]
            if total_carregado != len(dados):
                raise RuntimeError(
                    f"Esperadas {len(dados)} linhas, mas o banco retornou {total_carregado}."
                )

    print(f"Carga concluída: {total_carregado} linhas.")
    print("Indicadores SQL (falha, total, média 021, média 159, média 161):")
    for indicador in indicadores:
        print(indicador)


if __name__ == "__main__":
    main()