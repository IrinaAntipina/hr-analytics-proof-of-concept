with src_employer as (select * from {{ ref('src_employer') }})

select
    {{ dbt_utils.generate_surrogate_key(["employer_workplace", "workplace_city"]) }} as employer_id,

    max(employer_name) AS employer_name,
    max(employer_workplace) AS employer_workplace,
    max(workplace_street_address) AS workplace_street_address,
    max(workplace_region) AS workplace_region,
    max(workplace_city) AS workplace_city,
    max(workplace_postcode) AS workplace_postcode,
    max(workplace_country) AS workplace_country
    
from src_employer
group by employer_workplace, workplace_city