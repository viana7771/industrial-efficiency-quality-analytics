import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

root = Path(r'c:/Users/kaire/OneDrive/Área de Trabalho/Estudos/Industrial Efficiency & Quality Analytics')
raw = root / 'data' / 'raw'

padrao_rotulo = re.compile(r'^\s*(-?\d+)\s+"([^"]+)"\s*$')
linhas_rotulos = (raw / 'secom_labels.data').read_text(encoding='utf-8').splitlines()
rotulos_extraidos = [
    padrao_rotulo.match(linha).groups()
    for linha in linhas_rotulos
    if padrao_rotulo.match(linha)
]
rotulos = pd.DataFrame(rotulos_extraidos, columns=['rotulo', 'timestamp'])
rotulos['rotulo'] = rotulos['rotulo'].astype(int)
rotulos['timestamp'] = pd.to_datetime(rotulos['timestamp'], format='%d/%m/%Y %H:%M:%S')
rotulos['falha'] = (rotulos['rotulo'] == 1).astype(int)

d = pd.read_csv(raw / 'secom.data', sep=r'\s+', header=None, na_values='NaN', engine='python')
df = d.copy()
df['falha'] = rotulos['falha'].to_numpy()
missing = df.isna().mean()
cols_drop = df.columns[df.nunique(dropna=True) <= 1].union(missing[missing > 0.5].index)
df = df.drop(columns=cols_drop)
df = df.fillna(df.median(numeric_only=True))

features = [c for c in df.columns if c != 'falha']
rows = []

for c in features:
    aprovados = df.loc[df['falha'] == 0, c]
    falhas = df.loc[df['falha'] == 1, c]

    diff = falhas.mean() - aprovados.mean()
    pooled_var = (
        (aprovados.var(ddof=1) * (len(aprovados) - 1))
        + (falhas.var(ddof=1) * (len(falhas) - 1))
    ) / (len(aprovados) + len(falhas) - 2)
    pooled_std = np.sqrt(pooled_var) if pooled_var > 0 else 0.0
    d_cohen = 0.0 if pooled_std == 0 else diff / pooled_std

    t_stat, p_t = stats.ttest_ind(aprovados, falhas, equal_var=False, nan_policy='omit')
    u_stat, p_u = stats.mannwhitneyu(aprovados, falhas, alternative='two-sided', method='auto')

    rows.append(
        {
            'feature': c,
            'media_aprovados': aprovados.mean(),
            'media_falhas': falhas.mean(),
            'diff_media': diff,
            'abs_diff': abs(diff),
            'mediana_aprovados': aprovados.median(),
            'mediana_falhas': falhas.median(),
            'std_aprovados': aprovados.std(ddof=1),
            'std_falhas': falhas.std(ddof=1),
            'cohens_d': d_cohen,
            'p_ttest': p_t,
            'p_mannwhitney': p_u,
            't_stat': t_stat,
            'u_stat': u_stat,
        }
    )

ranking = pd.DataFrame(rows).sort_values('abs_diff', ascending=False)
print('TOP3')
print(
    ranking.head(3)[
        ['feature', 'media_aprovados', 'media_falhas', 'diff_media', 'mediana_aprovados', 'mediana_falhas', 'cohens_d', 'p_ttest', 'p_mannwhitney']
    ].to_string(index=False)
)
print('SHAPE', df.shape)
