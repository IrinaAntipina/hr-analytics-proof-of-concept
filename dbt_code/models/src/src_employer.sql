with stg_job_ads as (
    select * from {{ source('jobtech_analysis', 'stg_ads') }}
)

    select  
        employer__organization_number,
        employer__name as employer_name,
        employer__workplace as employer_workplace,
        workplace_address__street_address as workplace_street_address,
        workplace_address__region as workplace_region,
        workplace_address__municipality_code as workplace_postcode,
        workplace_address__municipality as workplace_city,

        workplace_address__country as workplace_country

    FROM
        stg_job_ads
    
    