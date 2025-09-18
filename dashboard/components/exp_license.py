# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from conn_warehouse import get_job_list

# def show_exp_data(table):
#     df = get_job_list(query=f"""SELECT * FROM {table}""")

#     exp = df['EXPERIENCE_REQUIRED'].value_counts()

#     fig_exp = px.pie(
#             values=exp.values, 
#             names=['Required' if x else 'Not required' for x in exp.index], 
#             title="",
#             hole=0.5,  # Donut style
#             color_discrete_sequence=["#F48720", "#b07cf4", '#45B7D1', '#96CEB4']
#         )
        
#     fig_exp.update_traces(
#         textposition='inside', 
#         textinfo='percent+label',
#         textfont_size=12,
#         marker=dict(line=dict(color='#FFFFFF', width=3))
#     )

#     fig_exp.update_layout(
#         height=280,
#         margin=dict(l=20, r=20, t=20, b=20),
#         showlegend=False,
#         font=dict(family="Arial", size=11),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)'
#     )

#     st.plotly_chart(fig_exp, use_container_width=True)


# def show_license_data(table):
#     df = get_job_list(query=f"""SELECT * FROM {table}""")

#     exp = df['DRIVING_LICENSE_REQUIRED'].value_counts()

#     fig_exp = px.pie(
#             values=exp.values, 
#             names=['Required' if x else 'Not required' for x in exp.index], 
#             title="",
#             hole=0.5,  # Donut style
#             color_discrete_sequence=["#F48720", "#b07cf4", "#F6F6F8", '#96CEB4']
#         )
        
#     fig_exp.update_traces(
#         textposition='inside', 
#         textinfo='percent+label',
#         textfont_size=12,
#         marker=dict(line=dict(color='#FFFFFF', width=3))
#     )

#     fig_exp.update_layout(
#         height=280,
#         margin=dict(l=20, r=20, t=20, b=20),
#         showlegend=False,
#         font=dict(family="Arial", size=11),
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)'
#     )

#     st.plotly_chart(fig_exp, use_container_width=True)


# def show_pie_chart(table):
#     col1, col2 = st.columns(2)
#     with col1:
#         show_exp_data(table)
#     with col2:
#         show_license_data(table)

import streamlit as st
import pandas as pd
import plotly.express as px
from conn_warehouse import get_job_list

def create_pie_chart(data, column_name, title):
    df_counts = pd.DataFrame({
        'category': ['Required', 'Not required'],
        'count': [
            data[data[column_name].isin([True, 1])].shape[0],
            data[data[column_name].isin([False, 0])].shape[0]
        ]
    })
    
    fig = px.pie(
        df_counts,
        values='count',
        names='category',
        title=title,
        hole=0.55,
        color='category',
        category_orders={'category': ['Required', 'Not required']},
        color_discrete_map={'Required': "#F48720", 'Not required': "#b07cf4"}
    )
    
    fig.update_traces(
        textposition='inside', 
        textinfo='percent',
        textfont_size=14,
        marker=dict(line=dict(color='#FFFFFF', width=3))
    )

    fig.update_layout(
        height=280,
        margin=dict(l=20, r=20, t=50, b=40),
        showlegend=True,
        legend=dict(
            orientation="h",
            y=-0.2,
            x=0.5,
            xanchor="center"
        ),
        font=dict(family="Arial", size=12),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title=dict(
            x=0.5,
            xanchor="center",
            font=dict(size=14, family="Arial Bold")
        )
    )
    
    return fig


def show_exp_data(table):
    df = get_job_list(query=f"""SELECT * FROM {table}""")
    fig = create_pie_chart(df, 'EXPERIENCE_REQUIRED', "Experience Required")
    st.plotly_chart(fig, use_container_width=True)


def show_license_data(table):
    df = get_job_list(query=f"""SELECT * FROM {table}""")
    fig = create_pie_chart(df, 'DRIVING_LICENSE_REQUIRED', "Driving License Required")
    st.plotly_chart(fig, use_container_width=True)


def show_pie_chart(table):
    col1, col2 = st.columns(2)
    with col1:
        show_exp_data(table)
    with col2:
        show_license_data(table)
