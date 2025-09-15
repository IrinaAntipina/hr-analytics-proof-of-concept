with src_job_details as (
    select * from {{ ref('src_job_details') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['id']) }} as job_details_id,
    id,
    max(headline) AS headline,
    max(description) AS description,
    max(description_html_formatted) AS description_html_formatted,
    max(employment_type) AS employment_type,
    max(duration) AS duration,
    max(salary_type) AS salary_type,
    max(scope_of_work_min) AS scope_of_work_min,
    max(scope_of_work_max) AS scope_of_work_max

from src_job_details
group by id