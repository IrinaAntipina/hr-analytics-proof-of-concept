with src_auxilliary_attributes as (select * from {{ ref('src_auxilliary_attributes') }})

select
    {{ dbt_utils.generate_surrogate_key(["id"]) }} as auxilliary_attribute_id,
    id,
    max(experience_required) AS experience_required,
    max(access_to_own_car) AS access_to_own_car,
    max(driving_license_required) AS driving_license_required

from src_auxilliary_attributes
group by id