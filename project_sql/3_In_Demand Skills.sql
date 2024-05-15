/***Question: What are the most in-demand skills for data analysts?**

- Identify the top 5 in-demand skills for a data analyst.
- Focus on all job postings.
- Why? Retrieves the top 5 skills with the highest demand in the job market
providing insights into the most valuable skills for job seekers.
*/

SELECT skills,count(sk.job_id) as demand_count
FROM job_postings_fact as j
inner join  skills_job_dim as sk on sk.job_id = j.job_id
LEFT JOIN skills_dim as s on s.skill_id = sk.skill_id
where job_title_short = 'Data Analyst' AND job_work_from_home = true
group by skills
order by demand_count DESC
limit 5 