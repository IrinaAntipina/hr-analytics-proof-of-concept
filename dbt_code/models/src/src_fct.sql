with stg_job_ads as (select * from {{ source('jobtech_analysis', 'stg_ads') }})

SELECT
    id, -- the thrre coulmns above will all make auxilliary_attributes_id and job_details_id
    employer__workplace,
    workplace_address__municipality, -- will be used as employer_id
    occupation__label, -- will be used as occupation_id
    number_of_vacancies as vacancies,
    relevance,
    application_deadline,
    publication_date

FROM
    stg_job_ads