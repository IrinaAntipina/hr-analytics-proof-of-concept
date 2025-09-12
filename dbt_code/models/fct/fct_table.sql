with fct_job_ads as (select * from {{ ref('src_fct') }})

select
    {{dbt_utils.generate_surrogate_key(["experience_required", "access_to_own_car", "driving_license_required"])}} as auxilliary_attribute_id,
    {{dbt_utils.generate_surrogate_key(["headline"])}} as job_details_id,
    {{dbt_utils.generate_surrogate_key(["employer__organization_number"])}} as employer_id,
    {{dbt_utils.generate_surrogate_key(["occupation__label"])}} as occupation_id,
    vacancies,
    relevance,
    application_deadline

from
    fct_job_ads