
with stg_job_ads as (
    select * from {{ source('jobtech_analysis', 'stg_ads') }}
)

   
select
    id,
    experience_required,
    access_to_own_car,
    driving_license_required

from stg_job_ads

