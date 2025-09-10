USE ROLE jobtech_team_role;
SELECT CURRENT_ROLE();

-- Check loaded data
USE DATABASE Jobtech_analysis;

SHOW SCHEMAS;
USE SCHEMA staging;
SHOW TABLES;


DESC TABLE staging.job_ads;

SELECT headline,employer__workplace,description__text
FROM staging.job_ads
LIMIT 10;

SELECT COUNT(*) AS total_job_ads
FROM staging.job_ads;
SELECT COUNT(DISTINCT employer__name) AS total_unique_employers
FROM staging.job_ads;
SELECT COUNT(DISTINCT employer__workplace) AS total_unique_workplaces
FROM staging.job_ads;

SELECT * FROM staging.job_ads WHERE EMPLOYER__WORKPLACE = 'LN Personal';

