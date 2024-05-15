/* **What are the top skills based on salary?** 

- Look at the average salary associated with each skill for Data Analyst positions.
- Focuses on roles with specified salaries, regardless of location.
- Why? It reveals how different skills impact salary levels for Data Analysts and helps identify
 the most financially rewarding skills to acquire or improve.
 */

select job_title_short,round(avg(salary_year_avg)) as salary_job,skills 
FROM job_postings_fact as j
inner join  skills_job_dim as sk on sk.job_id = j.job_id
LEFT JOIN skills_dim as s on s.skill_id = sk.skill_id
where job_title_short = 'Data Analyst'
and salary_year_avg  is NOT NULL
group by job_title_short, skills
order by salary_job DESC
limit 25