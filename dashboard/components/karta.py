import pandas as pd
import json
import numpy as np
import plotly.graph_objects as go
from conn_warehouse import get_job_list
from difflib import get_close_matches

def karta(table="mart_main", occupation=None):
    where_clause = f"WHERE occupation_field = '{occupation}'" if occupation else ""
    df = get_job_list(query=f"""
                            SELECT
                                sum(vacancies) as total_vacancies,
                                workplace_region
                            FROM
                                {table}
                            {where_clause}
                            GROUP BY workplace_region
                            ORDER BY total_vacancies DESC
                            """)
    
    with open("assets/swedish_regions.geojson", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    
    properties = [feature.get("properties") for feature in json_data.get("features")]
    region_codes = {
        prop.get("name"): str(prop.get("l_id"))  
        for prop in properties
        if prop and prop.get("name") and prop.get("l_id")  
    }
    
    return df, json_data, region_codes

def create_map(table="mart_main", occupation=None):
    
    df, json_data, region_codes = karta(table, occupation)

   # log_vacancies = np.log(df["TOTAL_VACANCIES"] + 1)
   # z_values = np.sqrt(df["TOTAL_VACANCIES"])

    z_values = df["TOTAL_VACANCIES"]
 
    matched_names = []
    for region in df["WORKPLACE_REGION"]:
        if region is None or region == "":  
            matched_names.append("")
            continue
            
        matches = get_close_matches(region, region_codes.keys(), n=1, cutoff=0.6)
        if matches:
            matched_names.append(matches[0])
        else:
            matched_names.append(region)
    
    region_ids = [region_codes.get(name, "") for name in matched_names]
    
    total_vacancies = df["TOTAL_VACANCIES"].sum()
 

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=json_data,
            locations=region_ids,
           # z=log_vacancies,
            z=z_values,
            featureidkey="properties.l_id", 
            colorscale="Oranges",
            zmin = 0,
            zmax = df["TOTAL_VACANCIES"].max(),
            showscale=True,  
            customdata=df["TOTAL_VACANCIES"],
            text=df["WORKPLACE_REGION"],
          
            marker_line_width=0.3,
        )
    )
    

    fig.update_layout(
        mapbox=dict(
            style="carto-positron",
            zoom=3.2, 
            center=dict(lat=62.6952, lon=13.9149)
        ),
        #width=600,
        #height=650,
        margin=dict(r=0, t=50, l=0, b=0),
        title=dict(
            text=f"""
                <br>
                <br><b>Total vacancies:</b>
                <br><b>{total_vacancies}</b>
                <br>
            """,
            x=0.06,
            y=0.75,
            font=dict(size=14, family="Arial"),
        ),
    )
    
    return fig

