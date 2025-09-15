USE ROLE USERADMIN;


CREATE ROLE IF NOT EXISTS jobtech_team_role;

CREATE ROLE IF NOT EXISTS jobtech_dlt_role;      
CREATE ROLE IF NOT EXISTS jobtech_dbt_role;      
CREATE ROLE IF NOT EXISTS jobtech_streamlit_role; 


GRANT USAGE ON WAREHOUSE job_analysis_wh TO ROLE jobtech_team_role;
GRANT OPERATE ON WAREHOUSE job_analysis_wh TO ROLE jobtech_team_role;
GRANT MONITOR ON WAREHOUSE job_analysis_wh TO ROLE jobtech_team_role;

GRANT USAGE ON DATABASE Jobtech_analysis TO ROLE jobtech_team_role;
GRANT CREATE SCHEMA ON DATABASE Jobtech_analysis TO ROLE jobtech_team_role;



GRANT ALL ON SCHEMA Jobtech_analysis.staging TO ROLE jobtech_team_role;
GRANT ALL ON SCHEMA Jobtech_analysis.warehouse TO ROLE jobtech_team_role;
GRANT ALL ON SCHEMA Jobtech_analysis.marts TO ROLE jobtech_team_role;
GRANT ALL ON SCHEMA Jobtech_analysis.public TO ROLE jobtech_team_role;


GRANT ALL ON ALL TABLES IN DATABASE Jobtech_analysis TO ROLE jobtech_team_role;


GRANT ALL ON FUTURE TABLES IN DATABASE Jobtech_analysis TO ROLE jobtech_team_role;


GRANT USAGE ON WAREHOUSE job_analysis_wh TO ROLE jobtech_dlt_role;
GRANT USAGE ON DATABASE Jobtech_analysis TO ROLE jobtech_dlt_role;
GRANT CREATE SCHEMA ON DATABASE Jobtech_analysis TO ROLE jobtech_dlt_role;
GRANT ALL ON SCHEMA Jobtech_analysis.staging TO ROLE jobtech_dlt_role;
GRANT ALL ON FUTURE TABLES IN SCHEMA Jobtech_analysis.staging TO ROLE jobtech_dlt_role;


GRANT USAGE ON WAREHOUSE job_analysis_wh TO ROLE jobtech_dbt_role;
GRANT USAGE ON DATABASE Jobtech_analysis TO ROLE jobtech_dbt_role;
GRANT USAGE ON SCHEMA Jobtech_analysis.staging TO ROLE jobtech_dbt_role;
GRANT SELECT ON ALL TABLES IN SCHEMA Jobtech_analysis.staging TO ROLE jobtech_dbt_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA Jobtech_analysis.staging TO ROLE jobtech_dbt_role;
GRANT ALL ON SCHEMA Jobtech_analysis.warehouse TO ROLE jobtech_dbt_role;
GRANT ALL ON SCHEMA Jobtech_analysis.marts TO ROLE jobtech_dbt_role;
GRANT ALL ON FUTURE TABLES IN SCHEMA Jobtech_analysis.warehouse TO ROLE jobtech_dbt_role;
GRANT ALL ON FUTURE VIEWS IN SCHEMA Jobtech_analysis.warehouse TO ROLE jobtech_dbt_role;
GRANT ALL ON FUTURE TABLES IN SCHEMA Jobtech_analysis.marts TO ROLE jobtech_dbt_role;
GRANT ALL ON FUTURE VIEWS IN SCHEMA Jobtech_analysis.marts TO ROLE jobtech_dbt_role;
GRANT CREATE SCHEMA ON DATABASE Jobtech_analysis TO ROLE jobtech_dbt_role;


GRANT USAGE ON WAREHOUSE job_analysis_wh TO ROLE jobtech_streamlit_role;
GRANT USAGE ON DATABASE Jobtech_analysis TO ROLE jobtech_streamlit_role;
GRANT USAGE ON SCHEMA Jobtech_analysis.marts TO ROLE jobtech_streamlit_role;
GRANT SELECT ON ALL TABLES IN SCHEMA Jobtech_analysis.marts TO ROLE jobtech_streamlit_role;
GRANT SELECT ON ALL VIEWS IN SCHEMA Jobtech_analysis.marts TO ROLE jobtech_streamlit_role;
GRANT SELECT ON FUTURE TABLES IN SCHEMA Jobtech_analysis.marts TO ROLE jobtech_streamlit_role;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA Jobtech_analysis.marts TO ROLE jobtech_streamlit_role;
GRANT SELECT ON TABLE Jobtech_analysis.marts.MART_MAIN TO ROLE jobtech_streamlit_role;




GRANT ROLE jobtech_team_role TO USER Irina;
GRANT ROLE jobtech_team_role TO USER Mohammad;
GRANT ROLE jobtech_team_role TO USER Alisher;
GRANT ROLE jobtech_team_role TO USER Andreas;

GRANT ROLE jobtech_streamlit_role TO USER Irina;
GRANT ROLE jobtech_streamlit_role TO USER Mohammad;
GRANT ROLE jobtech_streamlit_role TO USER Alisher;
GRANT ROLE jobtech_streamlit_role TO USER Andreas;

GRANT ROLE jobtech_dlt_role TO USER DLT_role;
GRANT ROLE jobtech_dbt_role TO USER DBT_role;
GRANT ROLE jobtech_streamlit_role TO USER Streamlit_role;


ALTER USER Irina SET DEFAULT_ROLE = 'jobtech_team_role';
ALTER USER Mohammad SET DEFAULT_ROLE = 'jobtech_team_role';
ALTER USER Alisher SET DEFAULT_ROLE = 'jobtech_team_role';
ALTER USER Andreas SET DEFAULT_ROLE = 'jobtech_team_role';
ALTER USER DLT_role SET DEFAULT_ROLE = 'jobtech_dlt_role';
ALTER USER DBT_role SET DEFAULT_ROLE = 'jobtech_dbt_role';
ALTER USER Streamlit_role SET DEFAULT_ROLE = 'jobtech_streamlit_role';



USE ROLE SYSADMIN;
USE DATABASE Jobtech_analysis;


USE ROLE SYSADMIN;
SHOW SCHEMAS IN DATABASE Jobtech_analysis;

SHOW TABLES IN SCHEMA Jobtech_analysis.STAGING;




USE ROLE jobtech_streamlit_role;
USE DATABASE JOBTECH_ANALYSIS;
USE SCHEMA MARTS;

SHOW TABLES;



SHOW TABLES IN SCHEMA Jobtech_analysis.marts;