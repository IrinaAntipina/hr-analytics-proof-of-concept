
with stg_job_ads as (   
    select *
    from {{ source('jobtech_analysis', 'stg_ads') }})


select  employer__organization_number as employer_id,
    employer__name,
    employer__url,
    employer__workplace,
    employer__phone_number
FROM
    stg_job_ads