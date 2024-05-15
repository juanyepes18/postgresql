/***What are the most optimal skills to learn (aka it’s in high demand and a high-paying skill) for a data analyst?** 

- Identify skills in high demand and associated with high average salaries for Data Analyst roles
- Concentrates on remote positions with specified salaries
- Why? Targets skills that offer job security (high demand) and financial benefits (high salaries),
 offering strategic insights for career development in data analysis
*/

with demand_skills AS(
SELECT
sk.skill_id,
s.skills,
count(sk.job_id) as demand_count
FROM 
job_postings_fact as j
inner join  skills_job_dim as sk on sk.job_id = j.job_id
LEFT JOIN skills_dim as s on s.skill_id = sk.skill_id
where j.job_title_short = 'Data Analyst'
AND j.job_work_from_home = true
AND j.salary_year_avg  is NOT NULL
group by sk.skill_id,s.skills

), average_salary as (
    select sk.skill_id,j.job_title_short,round(avg(salary_year_avg)) as salary_job,
    s.skills 
FROM job_postings_fact as j
inner join  skills_job_dim as sk on sk.job_id = j.job_id
LEFT JOIN skills_dim as s on s.skill_id = sk.skill_id
where j.job_title_short = 'Data Analyst'
and j.salary_year_avg  is NOT NULL
group by sk.skill_id,j.job_title_short,s.skills 
) 

SELECT
 ski.skill_id,
 avg.skills,
 demand_count,
 salary_job
from demand_skills as ski
inner join average_salary as avg on avg.skill_id = ski.skill_id
where
 demand_count > 10
order by
salary_job DESC,
demand_count DESC
LIMIT 25
 