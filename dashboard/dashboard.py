import streamlit as st
from components.top_employers import show_top_employers
from components.top_occupations import occupation_chart
from components.exp_license import show_exp_data
from components.karta import create_map

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

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
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 10px; color: white; margin-bottom: 20px;'>
            <h2>📊 Analytics</h2>
            <p style='margin: 0; opacity: 0.8;'>Dashboard</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        option = st.selectbox(
                "Occupation Field",
                chooser
            )
        st.markdown('</div>', unsafe_allow_html=True)

    # Main content
    st.markdown('<h1 class="dashboard-title">📊 Employment Analytics Dashboard</h1>', unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2, gap="large")
    col3, col4 = st.columns(2, gap="large")
    with col1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">💼 Top 10 Occupations</div>', unsafe_allow_html=True)
        st.pyplot(occupation_chart(mart_schema[option]))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🚗 Driver License & Experience</div>', unsafe_allow_html=True)
        show_exp_data(mart_schema[option])
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🗺️ Geographic Distribution</div>', unsafe_allow_html=True)
        st.map(create_map(mart_schema[option]))
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🏢 Top 10 Employers</div>', unsafe_allow_html=True)
        show_top_employers(mart_schema[option])
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    dashboard_page()