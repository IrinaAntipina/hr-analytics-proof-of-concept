import streamlit as st
import plotly.express as px
from conn_warehouse import get_job_list  

def get_top_employers(table):
    df_jobs = get_job_list(query=f"""
                            SELECT 
                                employer_name,
                                vacancies
                            FROM
                                {table}
                            """)

    df_top = df_jobs.groupby('EMPLOYER_NAME', as_index=False)['VACANCIES'].sum()
    df_top = df_top.sort_values(by='VACANCIES', ascending=False).head(10)
    return df_top

def show_top_employers(table='mart_main'):

    df_top = get_top_employers(table)

    fig = px.bar(
        df_top,
        x='EMPLOYER_NAME',
        y='VACANCIES',
        text='VACANCIES'
    )
    fig.update_traces(
        textposition='outside',
        textfont=dict(
            size=10,
            color='black'
        ),
        marker_color='#b07cf4'
    )
    fig.update_layout(
        yaxis={'categoryorder':'total ascending', 'showgrid': False},
        xaxis={'showgrid': False},
        plot_bgcolor='white',
        bargap=0.4,
        bargroupgap=0.05,

        xaxis_title={"text": "Employer Name",
                     'font': {'size': 14, 'color': 'black'}},

        yaxis_title={"text": "Number of Vacancies",
                     'font': {'size': 14, 'color': 'black'}},

        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
