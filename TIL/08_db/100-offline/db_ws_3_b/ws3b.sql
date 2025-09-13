-- applicants에서 username / applications에서 application_date, status / jobs에서 title, location
SELECT applicants.username, jobs.title, jobs.location, applications.application_date, applications.status
FROM applicants JOIN applications ON applicants.id = applications.applicant_id
JOIN jobs ON jobs.id = applications.job_id
WHERE applicants.username = 'john_doe';

-- applicants에서 username, email, phone / jobs에서 title / applications에서 application_date
SELECT applicants.username, applicants.email, applicants.phone, jobs.title, applications.application_date
FROM applicants JOIN applications ON applicants.id = applications.applicant_id
JOIN jobs ON jobs.id = applications.job_id
WHERE applications.status = 'Accepted';

-- jobs에서 title, department / applications에서 count(applicant_id) as applicant_count
SELECT jobs.title, jobs.department, COUNT(applications.applicant_id) as applicant_count
FROM jobs JOIN applications on jobs.id = applications.job_id
WHERE jobs.title LIKE 'Soft%'
GROUP BY jobs.title, jobs.department;

-- jobs에서 department / applications에서  count() status
SELECT jobs.department, count(applications.id) AS pending_count
FROM jobs JOIN applications ON applications.job_id = jobs.id
WHERE applications.status = 'Pending'
GROUP BY jobs.department;