with 
    fct_table as (select * from {{ref('fct_table')}}),
    dim_employer as (select * from {{ref('dim_employer')}}) ,
    dim_auxilliary as (select * from {{ref('dim_auxilliary_attributes')}}),
    dim_job_details as (select * from {{ref('dim_job_details')}}),
    dim_occupation as (select * from {{ref('dim_occupation')}})


select
    do.occupation,
    do.occupation_field,
    do.occupation_group,
    dj.headline,
    dj.description,
    dj.employment_type,
    dj.duration,
    dj.salary_type,
    da.experience_required,
    da.access_to_own_car,
    da.driving_license_required,
    de.employer_name,
    de.employer_workplace,
    de.workplace_street_address,
    de.workplace_region,
    de.workplace_city,
    de.workplace_postcode,
    de.workplace_country,
    ft.vacancies,
    ft.application_deadline,
    ft.publication_date
from
    fct_table ft
left join dim_employer de ON de.employer_id = ft.employer_id
left join dim_auxilliary da ON da.auxilliary_attribute_id = ft.auxilliary_attribute_id
left join dim_job_details dj ON dj.job_details_id = ft.job_details_id
left join dim_occupation do ON do.occupation_id = ft.occupation_id