import pandas as pd
import json
import numpy as np
import plotly.graph_objects as go
from conn_warehouse import get_job_list
from difflib import get_close_matches

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
                            """)
    
    with open("assets/swedish_regions.geojson", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    
    properties = [feature.get("properties") for feature in json_data.get("features")]
    region_codes = {
        prop.get("name"): prop.get("ref:se:länskod") for prop in properties
    }
    
    return df, json_data, region_codes

def create_map(table):
    
    df, json_data, region_codes = karta(table)
    log_vacancies = np.log(df["total_vacancies"] + 1)
    
    matched_names = [
        get_close_matches(region, region_codes.keys())[0] 
        if get_close_matches(region, region_codes.keys()) 
        else region  
        for region in df["workplace_region"]
    ]
    region_ids = [region_codes.get(name, "") for name in matched_names]
    
    total_vacancies = df["total_vacancies"].sum()
    top_occupation = df.iloc[0]["occupation"]  
    

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=json_data,
            locations=region_ids,
            z=log_vacancies,
            featureidkey="properties.ref:se:länskod",
            colorscale="Oranges",
            showscale=False,
            customdata=df["total_vacancies"],
            text=df["workplace_region"],
          
            marker_line_width=0.3,
        )
    )
    

    fig.update_layout(
        mapbox=dict(
            zoom=3.8, 
            center=dict(lat=62.6952, lon=13.9149)
        ),
        width=600,
        height=650,
        margin=dict(r=0, t=50, l=0, b=0),
        title=dict(
            text=f"""
                <br><b>{top_occupation}</b>
                <br>
                <br><b>{total_vacancies:,}</b>
                <br>
            """,
            x=0.06,
            y=0.75,
            font=dict(size=14, family="Arial"),
        ),
    )
    
    return fig

