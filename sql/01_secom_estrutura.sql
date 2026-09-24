-- =====================================================
-- SECOM - Estrutura inicial da base tratada
-- =====================================================

CREATE TABLE IF NOT EXISTS public.secom_tratado (
    id SERIAL PRIMARY KEY,
    falha SMALLINT NOT NULL CHECK (falha IN (0, 1)),
    feature_021 NUMERIC,
    feature_159 NUMERIC,
    feature_161 NUMERIC,
    feature_023 NUMERIC,
    feature_062 NUMERIC,
    feature_142 NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- Glossário de colunas da tabela tratada
-- =====================================================
CREATE TABLE IF NOT EXISTS public.secom_glossario_colunas (
    coluna_nome TEXT PRIMARY KEY,
    descricao TEXT NOT NULL,
    categoria TEXT NOT NULL,
    status_validacao TEXT NOT NULL,
    observacao TEXT
);

INSERT INTO public.secom_glossario_colunas (coluna_nome, descricao, categoria, status_validacao, observacao)
VALUES
    ('id', 'Identificador da observação na base tratada.', 'identificador', 'definido', 'Chave primária da tabela.'),
    ('falha', 'Indicador binário do resultado: 0 = aprovado, 1 = falha.', 'resultado', 'validado', 'Base para comparação entre grupos.'),
    ('feature_021', 'Feature selecionada como candidata relevante na análise exploratória e estatística.', 'feature', 'priorizada', 'Evidência estatística moderada a forte.'),
    ('feature_159', 'Feature com diferença observada entre grupos e potencial relevância analítica.', 'feature', 'candidata', 'Evidência estatística promissora, mas com validação complementar recomendada.'),
    ('feature_161', 'Feature investigada na etapa exploratória, mas sem sustentação estatística robusta.', 'feature', 'reavaliar', 'Diferenca observada não foi confirmada de forma estatisticamente consistente.'),
    ('feature_023', 'Feature complementar de apoio para exploração inicial do processo.', 'feature', 'suporte', 'Mantida para consulta e comparação.'),
    ('feature_062', 'Feature de apoio para exploração inicial.', 'feature', 'suporte', 'Mantida como coluna auxiliar na estrutura inicial.'),
    ('feature_142', 'Feature de apoio para exploração inicial.', 'feature', 'suporte', 'Mantida como coluna auxiliar na estrutura inicial.')
ON CONFLICT (coluna_nome) DO NOTHING;

-- =====================================================
-- Visão resumida para indicadores iniciais
-- =====================================================
CREATE OR REPLACE VIEW public.vw_secom_indicadores_top3 AS
SELECT
    falha,
    COUNT(*) AS total_observacoes,
    AVG(feature_021) AS media_feature_021,
    AVG(feature_159) AS media_feature_159,
    AVG(feature_161) AS media_feature_161,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_021) AS mediana_feature_021,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_159) AS mediana_feature_159,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_161) AS mediana_feature_161
FROM public.secom_tratado
GROUP BY falha;

-- =====================================================
-- Consultas úteis para a etapa inicial de SQL
-- =====================================================
-- 1) Distribuição por status
SELECT
    falha,
    COUNT(*) AS quantidade,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentual
FROM public.secom_tratado
GROUP BY falha;

-- 2) Comparação de médias por grupo
SELECT
    'feature_021' AS feature,
    AVG(feature_021) FILTER (WHERE falha = 0) AS media_aprovados,
    AVG(feature_021) FILTER (WHERE falha = 1) AS media_falhas,
    AVG(feature_021) FILTER (WHERE falha = 1) - AVG(feature_021) FILTER (WHERE falha = 0) AS diferenca_media
FROM public.secom_tratado
UNION ALL
SELECT
    'feature_159' AS feature,
    AVG(feature_159) FILTER (WHERE falha = 0) AS media_aprovados,
    AVG(feature_159) FILTER (WHERE falha = 1) AS media_falhas,
    AVG(feature_159) FILTER (WHERE falha = 1) - AVG(feature_159) FILTER (WHERE falha = 0) AS diferenca_media
FROM public.secom_tratado
UNION ALL
SELECT
    'feature_161' AS feature,
    AVG(feature_161) FILTER (WHERE falha = 0) AS media_aprovados,
    AVG(feature_161) FILTER (WHERE falha = 1) AS media_falhas,
    AVG(feature_161) FILTER (WHERE falha = 1) - AVG(feature_161) FILTER (WHERE falha = 0) AS diferenca_media
FROM public.secom_tratado;

-- 3) Comparação de medianas por grupo
SELECT
    'feature_021' AS feature,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_021) FILTER (WHERE falha = 0) AS mediana_aprovados,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_021) FILTER (WHERE falha = 1) AS mediana_falhas
FROM public.secom_tratado
UNION ALL
SELECT
    'feature_159' AS feature,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_159) FILTER (WHERE falha = 0) AS mediana_aprovados,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_159) FILTER (WHERE falha = 1) AS mediana_falhas
FROM public.secom_tratado
UNION ALL
SELECT
    'feature_161' AS feature,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_161) FILTER (WHERE falha = 0) AS mediana_aprovados,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY feature_161) FILTER (WHERE falha = 1) AS mediana_falhas
FROM public.secom_tratado;

-- =====================================================
-- Observações finais
-- =====================================================
-- Esta etapa inicial tem objetivo de preparar a base para consultas SQL e indicadores.
-- As features prioritárias foram definidas com base na análise exploratória e na validação estatística.
-- Em um próximo passo, a tabela pode ser expandida para incluir o restante das features tratadas.
