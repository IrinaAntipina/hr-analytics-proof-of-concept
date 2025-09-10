with stg_job_ads as (
    select * from {{ source('jobtech_analysis', 'stg_ads') }}
)

SELECT
    id,
    headline as job_details_key,
    external_id,
    label,
    webpage_url,
    logo_url,
    

    description__text as description,
    description__text_formatted as description_formatted,
    description__conditions as conditions,
    
    employment_type__concept_id as employment_type_concept_id,
    employment_type__label as employment_type,
    employment_type__legacy_ams_taxonomy_id as employment_type_legacy_id,
    
    salary_type__concept_id as salary_type_concept_id,
    salary_type__label as salary_type,
    salary_type__legacy_ams_taxonomy_id as salary_type_legacy_id,
    salary_description,
    
    duration__concept_id as duration_concept_id,
    duration__label as duration,
    duration__legacy_ams_taxonomy_id as duration_legacy_id,
    
    working_hours_type__concept_id as working_hours_concept_id,
    working_hours_type__label as working_hours_type,
    working_hours_type__legacy_ams_taxonomy_id as working_hours_legacy_id,
    
    scope_of_work__min as scope_work_min,
    scope_of_work__max as scope_work_max,

    experience_required,
    access_to_own_car,
    driving_license_required,
    
    publication_date,
    last_publication_date,
    removed,
    source_type

FROM stg_job_ads