import streamlit as st
from bar_chart import occupation_chart

chooser = ["Alla områden", "Installation, drift, underhåll", "Kropps- och skönhetsvård", "Kultur, media, design"]
mart_schema = {
    "Alla områden": "mart_main", 
    "Installation, drift, underhåll": "mart_idu",
    "Kropps- och skönhetsvård": "mart_ks",
    "Kultur, media, design": "mart_kmd"
}

Area = "Alla områden"

def main():
    st.markdown("En graf")

    area = st.selectbox("Välj område", chooser)

    st.pyplot(occupation_chart(mart_schema[area]))

if __name__ == "__main__":
    main()