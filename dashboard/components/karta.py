import pandas as pd
import json

from conn_warehouse import get_job_list


def karta(table="mart_main"):

    df = get_job_list(query=f"""
                            SELECT 
                                occupation,
                                sum(vacancies) as total_vacancies,
                                workplace_region
                            FROM
                                {table}
                            GROUP BY occupation, workplace_region
                            ORDER BY total_vacancies DESC
                            LIMIT 10
                            """).df()


    with open("assets/swedish_regions.geojson", "r", encoding="utf-8") as file:
        json_data = json.load(file)

    properties = [feature.get("properties") for feature in json_data.get("features")]

    region_codes = {
        prop.get("name"): prop.get("ref:se:länskod") for prop in properties
    }

    return df, json_data, region_codes