with stg_job_ads as (
    select * from {{ source('jobtech_analysis', 'stg_ads') }}
)


SELECT DISTINCT 
    
    occupation__label as occupation_label,
    occupation__concept_id as occupation_concept_id,
    occupation__label as occupation,
    occupation__legacy_ams_taxonomy_id as occupation_legacy_id,
    
    occupation_group__concept_id as occupation_group_concept_id,
    occupation_group__label as occupation_group,
    occupation_group__legacy_ams_taxonomy_id as occupation_group_legacy_id,
    
    occupation_field__concept_id as occupation_field_concept_id,
    occupation_field__label as occupation_field,
    occupation_field__legacy_ams_taxonomy_id as occupation_field_legacy_id

   

FROM stg_job_ads
WHERE occupation__label IS NOT NULL