import streamlit as st
from conn_warehouse import get_job_list
from components.top_employers import show_top_employers
from components.top_occupations import occupation_chart

chooser = ["Alla områden", "Installation, drift, underhåll", "Kropps- och skönhetsvård", "Kultur, media, design"]
mart_schema = {
    "Alla områden": "mart_main", 
    "Installation, drift, underhåll": "mart_idu",
    "Kropps- och skönhetsvård": "mart_ks",
    "Kultur, media, design": "mart_kmd"
}

def dashboard_page():
    st.set_page_config(page_title="Jobtech_Analysis",layout="wide")

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        option = st.selectbox(
                "Occupation Field",
                chooser
            )
        st.markdown('</div>', unsafe_allow_html=True)

    # Main content
    st.markdown(
        "<h1 style='text-align: center; color: blue;'>Jobtech Analysis </h1>",
        unsafe_allow_html=True
    )
    st.write("---")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.pyplot(occupation_chart(mart_schema[option]))   
    with col2:
        st.info("Other content here")
    with col3:
        st.info("Other content here")
    with col4:
        show_top_employers(mart_schema[option])

if __name__ == "__main__":
    dashboard_page()