{{
    config(
        materialized='incremental',
        unique_key='post_id',
        partition_by={
            "field": "created_at",
            "data_type": "timestamp",
            "granularity": "day"
        }
    )
}}

with source as (
    select * from {{ ref('stg_reddit_posts') }}
),

cleaned as (
    select
        id as post_id,
        {{ clean_text('title') }} as title,
        {{ clean_text('selftext') }} as content,
        author,
        score,
        num_comments,
        upvote_ratio,
        subreddit,
        timestamp_seconds(cast(created_utc as int64)) as created_at,
        {{ detect_language('selftext') }} as language,
        length(selftext) as content_length,
        array_length(split(selftext, ' ')) as word_count,
        extract(hour from timestamp_seconds(cast(created_utc as int64))) as hour_of_day,
        extract(dayofweek from timestamp_seconds(cast(created_utc as int64))) as day_of_week
    from source
    where id is not null
),

deduplicated as (
    select 
        *,
        row_number() over (partition by post_id order by created_at desc) as rn
    from cleaned
)

select 
    post_id,
    title,
    content,
    author,
    score,
    num_comments,
    upvote_ratio,
    subreddit,
    created_at,
    language,
    content_length,
    word_count,
    hour_of_day,
    day_of_week
from deduplicated
where rn = 1

{% if is_incremental() %}
  and created_at > (select max(created_at) from {{ this }})
{% endif %}
