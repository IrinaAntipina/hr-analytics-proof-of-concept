# HR Analytics Proof of Concept

This project demonstrates an **end-to-end data pipeline** and analytics workflow for HR data using:

- **DLT (Data Loading Tool)** for ingestion
- **dbt** for transformations
- **Streamlit** for dashboarding

---

## 🚀 Workflow

1. **Run the DLT pipeline**  
   Loads raw data into Snowflake.

2. **Run the dbt models**  
   Transforms raw data into analytics-ready tables.

3. **Run the Streamlit dashboard**  
   Visualizes the results.

---

## 🔑 Configuration

You need two configuration files to connect to Snowflake.  

### 1. `secrets.toml` (for DLT)
Create a file named `secrets.toml` inside your DLT project folder:

```toml
[destination.snowflake.credentials]
database = "<YOUR_DATABASE>"
username = "<YOUR_USERNAME>"
password = "<YOUR_PASSWORD>"
host = "<YOUR_ACCOUNT>"
warehouse = "<YOUR_WAREHOUSE>"
role = "<YOUR_ROLE>"
```

---

### 2. `.env` (for dbt + Streamlit)
Create a `.env` file in the root directory:

```env
SNOWFLAKE_USER="<YOUR_USERNAME>"
SNOWFLAKE_PASSWORD="<YOUR_PASSWORD>"
SNOWFLAKE_ACCOUNT="<YOUR_ACCOUNT>"
SNOWFLAKE_WAREHOUSE="<YOUR_WAREHOUSE>"
SNOWFLAKE_DATABASE="<YOUR_DATABASE>"
SNOWFLAKE_SCHEMA="<YOUR_SCHEMA>"
SNOWFLAKE_ROLE="<YOUR_ROLE>"
```

⚠️ **Do not commit these files to version control.** They contain sensitive information. Add them to your `.gitignore`.

---

## ⚙️ Installation

Clone the repo and install the dependencies:

```bash
git clone https://github.com/IrinaAntipina/hr-analytics-proof-of-concept.git
cd hr-analytics-proof-of-concept
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. **Run the DLT pipeline**  
   ```bash
   python dlt_pipeline.py
   ```

2. **Run dbt transformations**  
   ```bash
   dbt run
   ```

3. **Run the Streamlit dashboard**  
   ```bash
   streamlit run dashboard.py
   ```

---

## 📂 Repository Structure

```
.
├── dlt_pipeline.py       # Data ingestion into Snowflake
├── dbt_project/          # dbt models and configs
├── dashboard.py          # Streamlit dashboard
├── requirements.txt      # Python dependencies
├── secrets.toml          # (local only) Snowflake creds for DLT
└── .env                  # (local only) Snowflake creds for dbt + Streamlit
```

---

## ✅ Notes

- Run steps **in order**: **DLT ➝ dbt ➝ Streamlit**  
- Keep credentials secure (`.env` and `secrets.toml` must be in `.gitignore`)  
- Update Snowflake connection settings in your config files before running  
