-- bigquery/sentiment_analysis.sql

WITH raw_data AS (
  SELECT 
    id,
    text,
    created_at,
    -- Simulation d'une analyse de sentiment simplifiée
    CASE 
      WHEN REGEXP_CONTAINS(LOWER(text), r'bon|bien|super|crucial|top') THEN 'Positive'
      WHEN REGEXP_CONTAINS(LOWER(text), r'mauvais|nul|dommage|problème') THEN 'Negative'
      ELSE 'Neutral'
    END as sentiment_score
  FROM `${GCP_PROJECT_ID}.portfolio_silver.tweets_cleaned`
  WHERE _PARTITIONDATE = CURRENT_DATE()
)

SELECT 
  CURRENT_DATE() as date,
  sentiment_score,
  COUNT(*) as tweet_count,
  STRING_AGG(text, ' | ' LIMIT 3) as examples
FROM raw_data
GROUP BY sentiment_score;
