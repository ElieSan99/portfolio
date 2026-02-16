{% macro clean_text(column_name) %}
    regexp_replace(
        regexp_replace(
            regexp_replace(
                {{ column_name }},
                r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ''
            ), -- Remove URLs
            r'[\*\#\_\[\]\(\)\`]', ''
        ), -- Remove Markdown characters
        r'&amp;|&lt;|&gt;|&quot;', ''
    ) -- Remove HTML entities
{% endmacro %}
