with cleaned_posts as (
    select * from {{ ref('reddit_posts_cleaned') }}
),

ml_data as (
    select
        post_id,
        content as text_raw,
        title as title_raw,
        subreddit,
        hour_of_day,
        day_of_week,
        content_length,
        word_count,
        -- Weak supervision labels
        case 
            when score > 50 then 1 -- Positive/Hot
            when score < 10 then 0 -- Neutral/Low
            else null 
        end as label_hotness,
        case 
            when upvote_ratio > 0.9 then 1 -- Very positive
            when upvote_ratio < 0.7 then 0 -- Controversial
            else null
        end as label_sentiment
    from cleaned_posts
)

select * from ml_data
