with src_job_details as (
    select * from {{ ref('src_job_details') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['headline']) }} as job_details_id,
    headline,
    description,
    description_html_formatted,
    employment_type,
    duration,
    salary_type,
    scope_of_work_min,
    scope_of_work_max

from src_job_details