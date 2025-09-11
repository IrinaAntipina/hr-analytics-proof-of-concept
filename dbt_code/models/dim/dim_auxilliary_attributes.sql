with src_auxilliary_attributes as (select * from {{ ref('src_auxilliary_attributes') }})

select
    {{ dbt_utils.generate_surrogate_key(['auxiliary_attributes_id']) }} as auxilliary_attribute_id,
    experience_required,
    access_to_own_car,
    driving_license_required

from src_auxilliary_attributes