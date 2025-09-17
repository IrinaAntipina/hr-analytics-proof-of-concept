import streamlit as st
import plotly.express as px
from conn_warehouse import get_job_list  

def get_top_employers():
    df_jobs = get_job_list()

    df_top = df_jobs.groupby('EMPLOYER_NAME', as_index=False)['VACANCIES'].sum()
    df_top = df_top.sort_values(by='VACANCIES', ascending=False).head(10)
    return df_top

def show_top_employers():
    st.subheader("Top Ten Employers")

    df_top = get_top_employers()

    
    fig = px.bar(
        df_top,
        x='VACANCIES',
        y='EMPLOYER_NAME',
        #orientation='h',
        text='VACANCIES',
        #color='VACANCIES',
        color_continuous_scale='Blues'
    )
    fig.update_traces(
        textposition='outside',
        textfont=dict(
            size=12,
            color='black'
        )
    )
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        xaxis_title="Number of Vacancies",
        yaxis_title="Employer",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
