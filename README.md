# Industrial Efficiency & Quality Analytics

## Objetivo

Desenvolver um projeto profissional de Analytics aplicado a um processo industrial de fabricação de semicondutores, utilizando o dataset SECOM, do UCI Machine Learning Repository.

O projeto investigará padrões associados a falhas de qualidade e transformará as evidências encontradas em análises e indicadores úteis para o monitoramento do processo.

## Problema

Quais fatores observáveis do processo produtivo estão associados às falhas de qualidade e como os dados podem ser utilizados para monitorar e melhorar o processo?

A análise tratará as variáveis anonimizadas como variáveis técnicas do processo. Nenhum significado físico será atribuído sem suporte na documentação oficial ou em evidência verificável.

Associação estatística não será interpretada como causalidade. O projeto poderá identificar sinais e hipóteses para investigação, mas não substituirá uma investigação operacional ou experimental de causa.

## Escopo

### Escopo inicial

- obter os arquivos oficiais do dataset SECOM;
- validar a origem, integridade, formato e tamanho dos arquivos;
- entender a estrutura real dos dados antes de analisá-los;
- avaliar qualidade, ausências, duplicidades, variabilidade e distribuição do resultado;
- realizar tratamento justificado dos dados;
- conduzir análise exploratória em Python;
- aplicar estatística de forma gradual e explicada;
- construir consultas e indicadores em PostgreSQL;
- documentar hipóteses, evidências, limitações e decisões;
- manter o projeto local e reprodutível.

### Fora do escopo inicial

- dashboard ou Power BI;
- Machine Learning;
- afirmações de causalidade;
- remoção automática de dados;
- criação de uma arquitetura extensa sem necessidade comprovada.

Power BI e Machine Learning poderão ser avaliados futuramente, depois que a camada analítica estiver validada.

## Stack planejada

- **Python:** exploração, tratamento e análises;
- **Jupyter Notebook:** etapas de exploração, aprendizado e análise narrativa;
- **PostgreSQL:** armazenamento, consultas e indicadores SQL;
- **pgAdmin 4:** administração e consulta do PostgreSQL;
- **Ambiente Python:** ambiente virtual com `pyproject.toml`, possivelmente gerenciado por `uv`;
- **Git e GitHub:** versionamento desde o início, com commits pequenos e semanticamente claros.

A primeira versão utilizará PostgreSQL instalado localmente e administrado pelo pgAdmin 4. Docker não será introduzido inicialmente, pois não há necessidade concreta enquanto a instalação local atender ao projeto. Essa decisão poderá ser revisada caso surjam problemas de reprodução, configuração ou integração entre ambientes.

## Metodologia

O desenvolvimento seguirá ciclos curtos. Antes de cada nova etapa serão apresentados o objetivo, o conceito necessário, a estratégia e as decisões envolvidas. A implementação será feita gradualmente, com validação e documentação antes de avançar.

### Proteção de recursos e uso de memória

Antes de carregar qualquer arquivo no Python ou no Jupyter, serão verificados:

- tamanho físico do arquivo;
- formato e codificação;
- quantidade estimada de linhas e colunas;
- existência de múltiplos arquivos relacionados;
- representação de valores ausentes;
- memória necessária para uma leitura completa, quando puder ser estimada.

Nenhum arquivo será carregado integralmente sem uma avaliação prévia de tamanho e risco. Conforme o volume identificado, poderemos utilizar:

- leitura em chunks;
- processamento incremental;
- leitura somente das colunas necessárias;
- amostragem para inspeção inicial;
- cálculo de estatísticas sem manter toda a base na memória;
- conversão posterior para formatos mais eficientes;
- carregamento controlado no PostgreSQL.

Os arquivos originais serão preservados sem alterações. Toda transformação deverá ter justificativa, ser reproduzível e ser documentada.

### Etapas analíticas

1. entendimento do problema e das perguntas de negócio;
2. obtenção e validação da fonte oficial;
3. inspeção segura dos arquivos e entendimento dos dados;
4. avaliação sistemática da qualidade dos dados;
5. definição e aplicação documentada do tratamento;
6. análise exploratória orientada por perguntas;
7. introdução gradual de estatística aplicada;
8. armazenamento e análises no PostgreSQL;
9. consolidação de indicadores, conclusões e limitações;
10. avaliação posterior de visualização e Machine Learning, se fizer sentido.

Cada visualização ou consulta deverá responder a uma pergunta explícita. Testes estatísticos somente serão utilizados quando houver uma pergunta clara e o conceito, as premissas e a interpretação forem compreendidos.

## Roadmap

### Fase 1 — Planejamento e fonte de dados

- registrar objetivo, escopo e perguntas;
- consultar a documentação oficial do SECOM;
- obter os arquivos;
- verificar tamanho, formato e integridade;
- registrar origem, data de obtenção e limitações conhecidas.

### Fase 2 — Data Understanding

- identificar registros, variáveis e unidade de observação;
- verificar tipos e valores ausentes;
- analisar timestamps e resultado;
- medir duplicidades e variabilidade;
- documentar a estrutura real observada.

### Fase 3 — Data Quality

- investigar missing values, extremos e escalas;
- identificar variáveis constantes ou quase constantes;
- avaliar inconsistências;
- gerar um diagnóstico de qualidade sem remover dados automaticamente.

### Fase 4 — Tratamento

- definir regras para ausências e variáveis inutilizáveis;
- justificar transformações;
- criar uma camada processada reproduzível;
- validar as regras adotadas.

### Fase 5 — Análise exploratória

- comparar aprovação e falha;
- investigar padrões temporais;
- identificar variáveis candidatas;
- analisar estabilidade e possíveis grupos;
- registrar hipóteses e evidências.

### Fase 6 — Estatística aplicada

- explicar os conceitos antes da aplicação;
- avaliar diferenças entre grupos e associações;
- considerar tamanho de efeito e significância;
- distinguir relevância estatística de relevância operacional;
- evitar interpretações causais indevidas.

### Fase 7 — PostgreSQL e SQL

- definir o modelo de armazenamento;
- carregar os dados de forma controlada;
- criar consultas por finalidade;
- reproduzir análises selecionadas;
- construir indicadores de qualidade.

### Fase 8 — Conclusões

- responder às perguntas prioritárias;
- consolidar variáveis e padrões que merecem atenção;
- registrar hipóteses confirmadas e não confirmadas;
- propor indicadores e análises futuras;
- avaliar posteriormente Power BI ou Machine Learning.

## Limitações

- variáveis podem ser anonimizadas e não possuir significado físico documentado;
- a base pode conter muitos valores ausentes;
- o resultado pode estar desbalanceado;
- podem faltar informações de lote, máquina, turno, operador ou receita;
- um timestamp não garante uma série temporal completa ou sem interrupções;
- o dataset pode representar apenas um processo ou período específico;
- associações observadas não comprovam causalidade;
- resultados podem não generalizar para outras fábricas ou linhas;
- sem contexto operacional, algumas hipóteses não poderão ser confirmadas.

Essas limitações serão revisadas após a inspeção dos arquivos reais e da documentação oficial.

## Fonte dos dados

Dataset SECOM — UCI Machine Learning Repository:

[https://archive.ics.uci.edu/dataset/179/secom](https://archive.ics.uci.edu/dataset/179/secom)

Os arquivos originais somente serão incorporados após a verificação da fonte, do formato e das condições de uso. A documentação da obtenção será mantida junto ao projeto.

## Status atual

**Fase:** preparação da base para análise exploratória.

**Concluído:**

- objetivo e problema analítico definidos;
- escopo inicial delimitado;
- Python, Jupyter, PostgreSQL e pgAdmin 4 escolhidos;
- estratégia de versionamento definida;
- preocupação com tamanho dos arquivos e memória incorporada à metodologia;
- decisão inicial de não utilizar Docker, dashboard ou Machine Learning.
- fonte oficial e arquivos brutos do SECOM verificados;
- estrutura real confirmada em 1.567 observações e 590 features;
- interpretação do label documentada: `-1` = aprovação e `1` = falha;
- diagnóstico inicial concluído, incluindo ausências, duplicidades e variabilidade;
- tratamento inicial implementado em `notebooks/02_tratamento_dos_dados.ipynb`;
- base preparada com 446 features e nenhum valor ausente após o tratamento.

**Próximo passo:** iniciar a análise exploratória comparando as observações aprovadas e reprovadas, investigando padrões temporais e avaliando as distribuições das features tratadas.
