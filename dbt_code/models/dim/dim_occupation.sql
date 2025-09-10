with src_occupation as (
    select * from {{ ref('src_occupation') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['occupation']) }} as occupation_id,
    occupation,
    max(occupation_group) as occupation_group,
    max(occupation_field) as occupation_field,
    max(occupation_concept_id) as occupation_concept_id,
    max(occupation_group_concept_id) as occupation_group_concept_id,
    max(occupation_field_concept_id) as occupation_field_concept_id

from src_occupation
group by occupation