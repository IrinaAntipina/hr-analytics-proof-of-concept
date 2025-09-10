with src_job_details as (
    select * from {{ ref('src_job_details') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['headline']) }} as job_details_id,
    id,
    headline,
    external_id,
    label,
    webpage_url,
    logo_url,
    description,
    description_formatted,
    conditions,
    employment_type,
    salary_type,
    salary_description,
    duration,
    working_hours_type,
    scope_work_min,
    scope_work_max,
    experience_required,
    access_to_own_car,
    driving_license_required,
    publication_date,
    last_publication_date,
    removed,
    source_type

from src_job_details