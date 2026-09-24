from pathlib import Path
import re

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

root = Path(r'c:/Users/kaire/OneDrive/Área de Trabalho/Estudos/Industrial Efficiency & Quality Analytics')
pasta_dados = root / 'data' / 'raw'
caminho_dados = pasta_dados / 'secom.data'
caminho_rotulos = pasta_dados / 'secom_labels.data'

dados = pd.read_csv(caminho_dados, sep=r'\s+', header=None, na_values='NaN', engine='python')

padrao_rotulo = re.compile(r'^\s*(-?\d+)\s+"([^"]+)"\s*$')
linhas_rotulos = caminho_rotulos.read_text(encoding='utf-8').splitlines()
rotulos_extraidos = [
    padrao_rotulo.match(linha).groups()
    for linha in linhas_rotulos
    if padrao_rotulo.match(linha)
]
rotulos = pd.DataFrame(rotulos_extraidos, columns=['rotulo', 'timestamp'])
rotulos['rotulo'] = rotulos['rotulo'].astype(int)
rotulos['timestamp'] = pd.to_datetime(rotulos['timestamp'], format='%d/%m/%Y %H:%M:%S')
rotulos['falha'] = (rotulos['rotulo'] == 1).astype(int)

dados_tratados = dados.copy()
percentual_missing = dados_tratados.isna().mean()
colunas_constantes = dados_tratados.columns[dados_tratados.nunique(dropna=True) <= 1]
colunas_excesso_missing = percentual_missing[percentual_missing > 0.50].index
colunas_removidas = colunas_constantes.union(colunas_excesso_missing)
dados_tratados = dados_tratados.drop(columns=colunas_removidas)
medianas = dados_tratados.median(numeric_only=True)
dados_tratados = dados_tratados.fillna(medianas)
base_modelagem = dados_tratados.copy()
base_modelagem['falha'] = rotulos['falha'].to_numpy()

assert len(dados) == len(rotulos)
assert base_modelagem.isna().sum().sum() == 0
assert set(base_modelagem['falha'].unique()) <= {0, 1}

features = [col for col in base_modelagem.columns if col != 'falha']
linhas = []
for coluna in features:
    aprovados = base_modelagem.loc[base_modelagem['falha'] == 0, coluna]
    falhas = base_modelagem.loc[base_modelagem['falha'] == 1, coluna]
    linhas.append({
        'feature': coluna,
        'media_aprovados': aprovados.mean(),
        'media_falhas': falhas.mean(),
        'diff_media': falhas.mean() - aprovados.mean(),
        'std_aprovados': aprovados.std(ddof=1),
        'std_falhas': falhas.std(ddof=1),
    })
resumo_features = pd.DataFrame(linhas).sort_values('diff_media', ascending=False)
top_features = resumo_features.head(10).copy()
feature_exemplo = top_features['feature'].iloc[0]

ranking = []
for col in features:
    aprovados = base_modelagem.loc[base_modelagem['falha'] == 0, col]
    falhas = base_modelagem.loc[base_modelagem['falha'] == 1, col]
    media_aprovados = aprovados.mean()
    media_falhas = falhas.mean()
    diff_media = media_falhas - media_aprovados
    ranking.append({
        'feature': col,
        'media_aprovados': media_aprovados,
        'media_falhas': media_falhas,
        'diff_media': diff_media,
        'abs_diff': abs(diff_media),
        'mediana_aprovados': aprovados.median(),
        'mediana_falhas': falhas.median(),
        'std_aprovados': aprovados.std(ddof=1),
        'std_falhas': falhas.std(ddof=1),
    })
ranking_df = pd.DataFrame(ranking).sort_values('abs_diff', ascending=False)
selected_features = ranking_df.head(3)['feature'].tolist()

plt.figure(figsize=(10, 5))
sns.boxplot(data=base_modelagem, x='falha', y=feature_exemplo, palette='Set2')
plt.title(f'Comparação da feature: {feature_exemplo}')
plt.xlabel('Status')
plt.ylabel(feature_exemplo)
plt.xticks([0, 1], ['Aprovado', 'Falha'])
plt.show()

for feature in selected_features:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=base_modelagem, x='falha', y=feature, palette='Set2')
    plt.title(f'Gráfico: {feature}')
    plt.xlabel('Status')
    plt.ylabel(feature)
    plt.xticks([0, 1], ['Aprovado', 'Falha'])
    plt.tight_layout()
    plt.show()

print('validacao_ok')
print('shape_base:', base_modelagem.shape)
print('feature_exemplo:', feature_exemplo)
print('selected_features:', selected_features[:5])
