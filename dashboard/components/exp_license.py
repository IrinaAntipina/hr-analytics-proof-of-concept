import streamlit as st
import pandas as pd
import plotly.express as px
from conn_warehouse import get_job_list

def show_exp_data(table):
    df = get_job_list(query=f"""SELECT * FROM {table}""")

    exp = df['EXPERIENCE_REQUIRED'].value_counts()

    fig_exp = px.pie(
            values=exp.values, 
            names=['Required' if x else 'Not required' for x in exp.index], 
            title="",
            hole=0.5,  # Donut style
            color_discrete_sequence=["#F48720", "#b07cf4", '#45B7D1', '#96CEB4']
        )
        
    fig_exp.update_traces(
        textposition='inside', 
        textinfo='percent+label',
        textfont_size=12,
        marker=dict(line=dict(color='#FFFFFF', width=3))
    )

    fig_exp.update_layout(
        height=280,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        font=dict(family="Arial", size=11),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig_exp, use_container_width=True)


def show_license_data(table):
    df = get_job_list(query=f"""SELECT * FROM {table}""")

    exp = df['DRIVING_LICENSE_REQUIRED'].value_counts()

    fig_exp = px.pie(
            values=exp.values, 
            names=['Required' if x else 'Not required' for x in exp.index], 
            title="",
            hole=0.5,  # Donut style
            color_discrete_sequence=["#F48720", "#b07cf4", "#F6F6F8", '#96CEB4']
        )
        
    fig_exp.update_traces(
        textposition='inside', 
        textinfo='percent+label',
        textfont_size=12,
        marker=dict(line=dict(color='#FFFFFF', width=3))
    )

    fig_exp.update_layout(
        height=280,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        font=dict(family="Arial", size=11),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig_exp, use_container_width=True)


def show_pie_chart(table):
    col1, col2 = st.columns(2)
    with col1:
        show_exp_data(table)
    with col2:
        show_license_data(table)
