with stg_job_ads as (
    select * from {{ source('jobtech_analysis', 'stg_ads') }}
)


SELECT DISTINCT 
    
    occupation__label as occupation,

    occupation_group__label as occupation_group,
  
    occupation_field__label as occupation_field,
   
FROM stg_job_ads
WHERE occupation__label IS NOT NULL