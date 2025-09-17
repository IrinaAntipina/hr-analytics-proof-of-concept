import streamlit as st
from components.top_employers import show_top_employers
from components.top_occupations import occupation_chart





def dashboard_page():
    st.set_page_config(page_title="Jobtech_Analysis",layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: blue;'>Jobtech Analysis </h1>",
    unsafe_allow_html=True
)
st.write("---")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    show_top_employers()
       
with col2:
    occupation_chart()
with col3:
        st.info("Other content here")
with col4:
        st.info("Other content here")

