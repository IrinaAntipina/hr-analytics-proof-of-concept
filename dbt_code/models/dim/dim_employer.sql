with src_employer as (select * from {{ ref('src_employer') }})

select
    {{ dbt_utils.generate_surrogate_key(['employer__organization_number']) }} as employer_id,

    employer_id,
    employer_name,
    employer_workplace,
    workplace_address_street_address,
    workplace_address_region,
    workplace_address_municipality_code,
    workplace_address_municipality,
    workplace_address_country
from src_employer