select * from {{ source('raw_reddit', 'reddit_posts_ext') }}
