import matplotlib.pyplot as plt
import pandas as pd

# Datos proporcionados
data = [
    {"job_id": 387860, "job_title": "ERM Data Analyst", "salary_year_avg": 184000.0, "name_company": "Get It Recruit - Information Technology", "skills": "sql"},
    {"job_id": 387860, "job_title": "ERM Data Analyst", "salary_year_avg": 184000.0, "name_company": "Get It Recruit - Information Technology", "skills": "r"},
    {"job_id": 387860, "job_title": "ERM Data Analyst", "salary_year_avg": 184000.0, "name_company": "Get It Recruit - Information Technology", "skills": "python"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "excel"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "numpy"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "pandas"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "snowflake"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "go"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "sql"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "python"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "gitlab"},
    {"job_id": 1749593, "job_title": "Principal Data Analyst", "salary_year_avg": 186000.0, "name_company": "SmartAsset", "skills": "tableau"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "python"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "confluence"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "jira"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "atlassian"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "bitbucket"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "git"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "r"},
    {"job_id": 310660, "job_title": "Principal Data Analyst, AV Performance Analysis", "salary_year_avg": 189000.0, "name_company": "Motional", "skills": "sql"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "jenkins"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "sql"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "python"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "azure"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "aws"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "oracle"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "snowflake"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "tableau"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "power bi"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "sap"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "bitbucket"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "atlassian"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "jira"},
    {"job_id": 731368, "job_title": "Director, Data Analyst - HYBRID", "salary_year_avg": 189309.0, "name_company": "Inclusively", "skills": "confluence"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "tableau"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "gitlab"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "sql"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "python"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "go"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "snowflake"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "pandas"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "numpy"},
    {"job_id": 168310, "job_title": "Principal Data Analyst (Remote)", "salary_year_avg": 205000.0, "name_company": "SmartAsset", "skills": "excel"},
    {"job_id": 127084, "job_title": "Data Analyst - Health Equity", "salary_year_avg": 206000.0, "name_company": "Yuvo Health", "skills": "stata"},
    {"job_id": 127084, "job_title": "Data Analyst - Health Equity", "salary_year_avg": 206000.0, "name_company": "Yuvo Health", "skills": "sql"},
    {"job_id": 127084, "job_title": "Data Analyst - Health Equity", "salary_year_avg": 206000.0, "name_company": "Yuvo Health", "skills": "r"},
    {"job_id": 127084, "job_title": "Data Analyst - Health Equity", "salary_year_avg": 206000.0, "name_company": "Yuvo Health", "skills": "python"}
]

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Agrupar los datos por 'job_title' y calcular el salario promedio
job_salary = df.groupby('job_title')['salary_year_avg'].mean().reset_index()

# Crear la gráfica
plt.figure(figsize=(12, 8))
plt.barh(job_salary['job_title'], job_salary['salary_year_avg'], color='skyblue')
plt.xlabel('Average salary year ($)', fontsize=12)
plt.ylabel('Job title ', fontsize=12)
plt.title('Top Paying Data Analyst Jobs')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
