with stg_job_ads as (select * from {{ source('jobtech_analysis', 'stg_ads') }})

SELECT
    experience_required,
    access_to_own_car,
    driving_license_required, -- the thrre coulmns above will all make auxilliary_attributes_id
    headline, -- will be used as job_details_id
    employer__organization_number, -- will be used as employer_id
    occupation__label, -- will be used as occupation_id
    number_of_vacancies as vacancies,
    relevance,
    application_deadline
FROM
    stg_job_ads