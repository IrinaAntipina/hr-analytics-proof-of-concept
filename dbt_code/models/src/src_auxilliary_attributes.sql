with stg_job_ads as (  select *
    from {{ source('jobtech_analysis', 'stg_ads') }})

select 
     *
from stg_job_ads
