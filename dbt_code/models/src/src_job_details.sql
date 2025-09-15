with stg_job_ads as (
    select * from {{ source('jobtech_analysis', 'stg_ads') }}
)

SELECT
    id,
    headline,
 
    description__text as description,
    description__text_formatted as description_html_formatted,
    
    employment_type__label as employment_type,

    duration__label as duration,
    
    salary_type__label as salary_type,
    
    scope_of_work__min as scope_of_work_min,
    scope_of_work__max as scope_of_work_max

FROM stg_job_ads