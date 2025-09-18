with fct_job_ads as (select * from {{ ref('src_fct') }})

select
    {{dbt_utils.generate_surrogate_key(["id"])}} as auxilliary_attribute_id,
    {{dbt_utils.generate_surrogate_key(["id"])}} as job_details_id,
    {{dbt_utils.generate_surrogate_key(["employer__workplace", "workplace_address__municipality"])}} as employer_id,
    {{dbt_utils.generate_surrogate_key(["occupation__label"])}} as occupation_id,
    vacancies,
    relevance,
    application_deadline,
    publication_date

from
    fct_job_ads