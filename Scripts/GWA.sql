SELECT application_type, 
       case_no, 
       case_status, 
       class_of_admission, 
       country_of_citzenship, 
       decision_date, 
       employer_address_1, 
       employer_address_2, 
       employer_city, 
       employer_name, 
       employer_num_employees, 
       employer_postal_code, 
       employer_state, 
       job_info_work_city, 
       job_info_work_postal_code, 
       job_info_work_state, 
       naics_2007_us_code, 
       naics_2007_us_title, 
       naics_code, 
       pw_amount_9089, 
       pw_job_title_9089, 
       pw_level_9089, 
       pw_soc_code, 
       pw_soc_title, 
       pw_source_name_9089, 
       pw_unit_of_pay_9089, 
       us_economic_sector, 
       wage_offer_from_9089, 
       wage_offer_to_9089, 
       wage_offer_unit_of_pay_9089
FROM visas.global_workforce_analysis;

#2 Top 20 Employers
SELECT employer_name, COUNT(*) AS visa_applications
FROM visas.global_workforce_analysis
WHERE case_status = 'Certified'
GROUP BY employer_name
ORDER BY visa_applications DESC
LIMIT 20;

#3 Top 20 Countries
SELECT country_of_citzenship, COUNT(*) AS visa_applications
FROM visas.global_workforce_analysis
WHERE case_status = 'Certified'
GROUP BY country_of_citzenship
ORDER BY visa_applications DESC
LIMIT 20;

#4 Top 20 Industries
SELECT naics_2007_us_title, COUNT(*) AS visa_applications
FROM visas.global_workforce_analysis
WHERE case_status = 'Certified'
GROUP BY naics_2007_us_title
ORDER BY visa_applications DESC
LIMIT 20;

#5 Top 20 Cities
SELECT employer_city, COUNT(*) AS visa_applications
FROM visas.global_workforce_analysis
WHERE case_status = 'Certified'
GROUP BY employer_city
ORDER BY visa_applications DESC
LIMIT 20;


WITH employer_rank AS (
    SELECT employer_name, COUNT(*) AS visa_applications,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rn
    FROM visas.global_workforce_analysis
    WHERE case_status = 'Certified'
    GROUP BY employer_name
    ORDER BY visa_applications DESC
    LIMIT 20
),
industry_rank AS (
    SELECT naics_2007_us_title, COUNT(*) AS visa_applications,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rn
    FROM visas.global_workforce_analysis
    WHERE case_status = 'Certified'
    GROUP BY naics_2007_us_title
    ORDER BY visa_applications DESC
    LIMIT 20
),
country_rank AS (
    SELECT country_of_citzenship, COUNT(*) AS visa_applications,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rn
    FROM visas.global_workforce_analysis
    WHERE case_status = 'Certified' AND country_of_citzenship IS NOT NULL
    GROUP BY country_of_citzenship
    ORDER BY visa_applications DESC
    LIMIT 20
),
city_rank AS (
    SELECT employer_city, COUNT(*) AS visa_applications,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS rn
    FROM visas.global_workforce_analysis
    WHERE case_status = 'Certified'
    GROUP BY employer_city
    ORDER BY visa_applications DESC
    LIMIT 20
)

SELECT 
    e.employer_name AS `Employer Name`, e.visa_applications AS `Visa Applications`,
    i.naics_2007_us_title AS `Industry Name`, i.visa_applications AS `Industry Applications`,
    c.country_of_citzenship AS `Country Name`, c.visa_applications AS `Country Applications`,
    ci.employer_city AS `City Name`, ci.visa_applications AS `City Applications`
FROM employer_rank e
LEFT JOIN industry_rank i ON e.rn = i.rn
LEFT JOIN country_rank c ON e.rn = c.rn
LEFT JOIN city_rank ci ON e.rn = ci.rn;
