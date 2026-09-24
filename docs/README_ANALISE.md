# Resumo da análise exploratória

## Objetivo
Comparar as observações aprovadas e reprovadas da base SECOM tratada para identificar variáveis que mais diferenciam os grupos e preparar a base para a próxima fase de estatística aplicada.

## Base avaliadas
- base original validada em 1.567 observações e 590 features;
- base tratada reduzida para 446 features;
- ausência de valores faltantes após imputação mediana;
- remoção de colunas constantes e de colunas com excesso de ausências.

## Resultado principal
As três variáveis mais relevantes identificadas foram:

1. Feature 161
2. Feature 159
3. Feature 21

Essas colunas compõem o conjunto de candidatos mais promissores para diferenciação entre grupos.

## Interpretação
- Feature 161 foi a principal variável com maior separação observada entre aprovação e falha.
- Feature 159 também mostrou diferença consistente e deve ser tratada como forte sinal analítico.
- Feature 21 aparece como terceira candidata relevante, com contraste menor, mas ainda importante para a etapa de validação estatística.

## Limitações
- as variáveis são anônimas;
- não há significado físico documentado sem suporte externo;
- a leitura é de associação observada e não de causalidade;
- o resultado precisa ser validado em estatística aplicada e em contexto operacional.

## Próximo passo
Executar análise estatística sobre as variáveis prioritárias, validar tamanho de efeito e preparar indicadores para a etapa em SQL.
