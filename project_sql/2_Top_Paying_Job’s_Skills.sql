/***Question: What are the top-paying data analyst jobs, and what skills are required?** 

- Identify the top 10 highest-paying Data Analyst jobs and the specific skills required for these roles.
- Filters for roles with specified salaries that are remote
- Why? It provides a detailed look at which high-paying jobs demand certain skills, 
helping job seekers understand which skills to develop that align with top salaries*/


with top_paying_jobs as (SELECT
	j.job_id,
	j.job_title,
	j.salary_year_avg,
    c.name as name_company
from job_postings_fact as j
left JOIN company_dim as c on j.company_id = c.company_id
where job_title_short = 'Data Analyst' and
job_location = 'Anywhere' AND
salary_year_avg is NOT NULL
order by salary_year_avg DESC
limit 10)

SELECT t.*,s.skills FROM top_paying_jobs as t
inner join  skills_job_dim as sk on sk.job_id = t.job_id
LEFT JOIN skills_dim as s on s.skill_id = sk.skill_id
ORDER BY salary_year_avg	
