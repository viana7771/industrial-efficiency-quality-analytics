# Estatística aplicada das 3 features prioritárias

## Objetivo
Validar se as variáveis selecionadas na análise exploratória mantêm diferença relevante entre os grupos de aprovado e falha após o tratamento da base.

## Base usada
- base tratada com 1.567 observações e 447 colunas;
- remoção de colunas constantes e com excesso de ausências;
- imputação por mediana das variáveis restantes;
- comparação entre grupos: falha = 1 e aprovado = 0.

## Resultado da validação

### 1) Feature 161
- média aprovados: 4087.89
- média falhas: 3742.98
- diferença: -344.91
- p-value T-test: 0.323997
- p-value Mann-Whitney: 0.703006
- Cohen's d: -0.0814

Conclusão: a diferença observada não se mostrou estatisticamente robusta. A feature 161 não deve ser priorizada como evidência forte na fase atual.

### 2) Feature 159
- média aprovados: 862.11
- média falhas: 1167.03
- diferença: 304.92
- p-value T-test: 0.034733
- p-value Mann-Whitney: 0.057279
- Cohen's d: 0.3112

Conclusão: há evidência de diferença moderada. O resultado é promissor, mas ainda está próximo do limiar de significância em teste não paramétrico, então deve ser tratada como hipótese relevante e candidata a validação adicional.

### 3) Feature 21
- média aprovados: -5636.36
- média falhas: -5363.82
- diferença: 272.54
- p-value T-test: 0.004541
- p-value Mann-Whitney: 0.000468
- Cohen's d: 0.4375

Conclusão: esta é a feature com evidência mais consistente. A diferença entre grupos é estatisticamente relevante e apresenta efeito moderado, sendo a candidata principal para continuar para a próxima fase.

## Interpretação geral
A etapa exploratória identificou três sinais prioritários, mas a validação estatística mostrou que o comportamento não é uniforme entre eles:

- Feature 21: reforçada como sinal mais forte e relevante;
- Feature 159: sinal interessante e promissor, porém com validação mais delicada;
- Feature 161: não sustentou robustez estatística nesta análise e deve receber menor peso.

## Próximo passo recomendado
1. manter Feature 21 como principal candidata;
2. reavaliar Feature 159 em contexto operacional e com análise complementar;
3. não priorizar Feature 161 como evidência forte no momento;
4. preparar a estrutura de indicadores e SQL para as colunas com melhor suporte estatístico.

## Observação final
A análise continua sendo orientada por associação observada e não por causalidade. O objetivo da etapa atual é reduzir ruído e decidir quais variáveis merecem continuidade no fluxo analítico e no armazenamento em SQL.
