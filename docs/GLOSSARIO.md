# Glossário do Projeto

## 1. Glossário de domínio do projeto

### Aprovado
Observação cujo label foi registrado como aprovação, segundo a classificação original do dataset SECOM. No projeto, esse grupo é tratado como o conjunto de registros sem falha detectada.

### Falha
Observação cujo label foi registrado como falha no processo. Essa categoria é a base da análise comparativa com o grupo de aprovação.

### Feature
Variável observável do processo, geralmente numérica, que compõe a base de dados e será analisada em relação ao resultado (aprovação ou falha).

### Label
Variável de resultado, também chamada de alvo. No SECOM, representa a classificação qualitativa da observação: aprovação ou falha.

### Base tratada
Conjunto de dados após a aplicação das regras de limpeza, remoção de colunas sem informação e imputação de valores ausentes.

### Feature candidata
Variável que mostra diferença relevante entre os grupos comparados e, por isso, merece atenção na próxima etapa analítica.

### Anonimização
Processo em que as variáveis não têm nomes operacionais ou físicos explícitos. No projeto, isso impede atribuir significado físico direto às colunas sem evidência documental.

### Relevância operacional
Medida de quão útil uma variável pode ser para monitoramento e diagnóstico, mesmo quando ainda não é possível afirmar causalidade.

### Relevância estatística
Diferença percebida entre grupos que pode ser validada por ferramentas estatísticas. Nem toda diferença estatística implica impacto prático.

### Causalidade
Relação de causa e efeito. O projeto evita afirmar causalidade sem investigação operacional, experimental ou documental adicional.

### Observação
Cada linha da base, representando um registro do processo ou do fenômeno observado.

### Tratamento dos dados
Conjunto de regras aplicadas para adequar a base à análise, como remoção de colunas constantes, remoção de colunas com excesso de ausências e imputação de valores faltantes.

### Imputação
Substituição de valores ausentes por um valor plausível, como a mediana da coluna, para manter a base coerente para análise.

### Fase exploratória
Etapa em que se comparam grupos, se observam distribuições e se identificam variáveis com potencial de diferenciação.

### Fase estatística aplicada
Etapa posterior em que testes e medidas de efeito são utilizados para validar melhor a força das relações observadas.

### Indicador SQL
Consulta ou cálculo preparado para ser reutilizado em banco de dados, com foco em monitoramento e comparação entre grupos.

---

## 2. Glossário técnico

### Python
Linguagem principal usada para análise, tratamento, validação e exploração dos dados.

### Jupyter Notebook
Ambiente interativo usado para documentar etapas de código, visualização e interpretação.

### Pandas
Biblioteca Python para manipulação e análise de estruturas tabulares, como DataFrames.

### NumPy
Biblioteca para operações numéricas eficientes e suporte matemático em arrays.

### Matplotlib
Biblioteca usada para construir gráficos e visualizações estáticas.

### Seaborn
Biblioteca com visualização estatística mais amigável e com maior foco em análise exploratória.

### DataFrame
Estrutura tabular do Pandas, semelhante a uma tabela em memória.

### Missing value
Valor ausente ou nulo em uma variável. Também chamado de dado faltante.

### Coluna constante
Variável em que quase todos os valores são iguais, o que reduz seu poder explicativo.

### Coluna com excesso de ausências
Variável com proporção muito alta de valores faltantes, sendo difícil ou pouco confiável para análise.

### Mediana
Valor central de uma distribuição, usado como referência robusta para imputação em colunas numéricas.

### Desvio padrão
Medida de dispersão que indica o quanto os valores se afastam da média.

### Média
Valor central da distribuição, calculado somando os valores e dividindo pela quantidade de observações.

### Diferença de médias
Comparação entre a média de um grupo e a média de outro grupo para avaliar separação.

### Ranking de features
Ordenação das variáveis por potencial de diferenciação entre grupos.

### Regressão
Técnica estatística ou preditiva para modelar relações entre variáveis. Não é foco imediato deste projeto.

### SQL
Linguagem de consulta usada para manipular e consultar dados em bancos relacionais.

### PostgreSQL
Sistema de banco de dados relacional usado como camada de armazenamento e consulta.

### pgAdmin 4
Ferramenta gráfica para administração e consulta do PostgreSQL.

### Ambiente virtual
Ambiente isolado do Python para manter dependências e versões consistentes do projeto.

### Commit
Registro do estado atual do projeto no versionamento Git, com mensagem descritiva.

### Push
Envio dos commits locais para o repositório remoto no GitHub.

### Branch
Linha de desenvolvimento do projeto no Git. Neste projeto, o uso principal é manter a ramificação principal atualizada com incrementos documentados.

### Versionamento
Controle de alterações do projeto ao longo do tempo, permitindo rastrear histórico, decisões e evoluções.

---

## 3. Glossário das colunas principais

### id
Identificador da observação dentro da base tratada.

### falha
Indicador binário do resultado da amostra:
- 0 = aprovado
- 1 = falha

### feature_021
Uma das variáveis com diferença observada entre os grupos; candidata relevante para análise.

### feature_159
Variável com forte contraste entre aprovados e falhas, destacada pela análise exploratória.

### feature_161
Variável com maior diferença observada de média entre os grupos, sendo uma das principais candidatas da fase exploratória.

### timestamp
Marca temporal da observação, quando disponível, usada para inspeção temporal e análise de sequência.

### feature_xxx
Convenção técnica para referenciar colunas numéricas anônimas do dataset após o tratamento inicial.

---

## 4. Observações importantes

- O projeto mantém as variáveis como anônimas e técnicas, sem atribuir significados físicos sem suporte documental.
- A principal leitura é de associação observada, e não de causalidade.
- O glossário foi criado para facilitar o entendimento contínuo do projeto, especialmente em fases de análise, documentação, SQL e revisão do roadmap.
- O objetivo deste documento é servir como guia de referência rápida para a equipe e para o próprio projeto em futuras sessões de trabalho.
