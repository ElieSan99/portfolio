with cleaned_posts as (
    select * from {{ ref('reddit_posts_cleaned') }}
),

keywords as (
    select
        post_id,
        created_at,
        subreddit,
        case 
            when regexp_contains(lower(content), r'\bpython\b') then 'Python'
            when regexp_contains(lower(content), r'\bsql\b') then 'SQL'
            when regexp_contains(lower(content), r'\bdbt\b') then 'dbt'
            when regexp_contains(lower(content), r'\bterraform\b') then 'Terraform'
            when regexp_contains(lower(content), r'\bairflow\b') then 'Airflow'
            when regexp_contains(lower(content), r'\bspark\b') then 'Spark'
            when regexp_contains(lower(content), r'\baws\b') then 'AWS'
            when regexp_contains(lower(content), r'\bgcp\b') then 'GCP'
            when regexp_contains(lower(content), r'\blooker\b') then 'Looker'
            when regexp_contains(lower(content), r'\btableau\b') then 'Tableau'
        end as tech_mention
    from cleaned_posts
),

daily_tech_counts as (
    select
        date(created_at) as event_date,
        tech_mention,
        count(*) as mention_count
    from keywords
    where tech_mention is not null
    group by 1, 2
),

rolling_metrics as (
    select
        *,
        avg(mention_count) over (
            partition by tech_mention 
            order by event_date 
            rows between 6 preceding and current row
        ) as rolling_avg_7d
    from daily_tech_counts
)

select * from rolling_metrics
