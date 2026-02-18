with cleaned_posts as (
    select * from {{ ref('reddit_posts_cleaned') }}
),

daily_metrics as (
    select
        date(created_at) as event_date,
        subreddit,
        language,
        count(*) as total_posts,
        avg(score) as avg_score,
        avg(upvote_ratio) as avg_upvote_ratio,
        sum(num_comments) as total_comments
    from cleaned_posts
    group by 1, 2, 3
)

select * from daily_metrics
