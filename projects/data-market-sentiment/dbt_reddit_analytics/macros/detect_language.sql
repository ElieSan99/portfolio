{% macro detect_language(column_name) %}
    case 
        when regexp_contains(lower({{ column_name }}), r'\b(le|la|les|un|une|des|et|ou|est|sont|dans|pour|avec|sur)\b') then 'fr'
        else 'en' -- Par défaut en, à affiner si besoin
    end
{% endmacro %}
