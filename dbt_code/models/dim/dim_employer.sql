with src_employer as (select * from {{ ref('src_employer') }})

select
    {{ dbt_utils.generate_surrogate_key(["employer_workplace", "workplace_city"]) }} as employer_id,

    employer_name,
    employer_workplace,
    workplace_street_address,
    workplace_region,
    workplace_city,
    workplace_postcode,
    workplace_country
    
from src_employer