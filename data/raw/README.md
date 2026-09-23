# Dados brutos do SECOM

## Origem

- Dataset: SECOM
- Fonte oficial: UCI Machine Learning Repository
- Página: <https://archive.ics.uci.edu/dataset/179/secom>
- Download utilizado: <https://archive.ics.uci.edu/static/public/179/secom.zip>
- Data de obtenção: 2026-09-23
- Licença informada pelo UCI: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Referência: McCann, M. & Johnston, A. (2008). SECOM [Dataset]. UCI Machine Learning Repository. DOI: <https://doi.org/10.24432/C54305>

## Arquivos obtidos

| Arquivo | Tamanho aproximado | Descrição inicial |
|---|---:|---|
| `secom.data` | 5,4 MB | Medições técnicas do processo em formato texto, separadas por espaços |
| `secom_labels.data` | 39,7 KB | Rótulo de qualidade e timestamp de cada observação |
| `secom.names` | 4,1 KB | Documentação fornecida junto ao dataset |
| `secom.zip` | 2,0 MB | Arquivo compactado original obtido da fonte oficial |

## Validação inicial

Validações realizadas sem carregar os dados no Python ou no Jupyter:

- `secom.data` possui 1.567 linhas;
- `secom_labels.data` possui 1.567 linhas;
- todas as linhas verificadas de `secom.data` possuem 590 valores separados por espaço;
- todas as linhas de `secom_labels.data` seguem o formato `rótulo "timestamp"`;
- os rótulos observados utilizam `-1` e `1`;
- os valores ausentes aparecem representados como `NaN`;
- a primeira linha de rótulo contém `-1` e o timestamp `19/07/2008 11:55:00`;
- o hash SHA-256 do arquivo `secom.zip` é `EEA568BAF3C2229096D7D294CF0B096B5502BD96D92C0B80A65B84714059BE8E`.

## Divergência a investigar

A página oficial do UCI informa 591 features, mas a inspeção física de `secom.data` encontrou 590 valores em cada uma das 1.567 linhas. Essa divergência será investigada durante o Data Understanding antes de definir nomes, tipos ou interpretações das colunas.

Nenhuma coluna foi removida, renomeada ou transformada nesta etapa.