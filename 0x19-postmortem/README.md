Duration Date and time of the outage: February 17, 2024, 10:00 a.m. to 12:00 p.m. 
Impact During this period, approximately 30% of users experienced slow loading and occasional errors while using the main web application.

## Root Cause
The root cause of the problem was a database deadlock issue caused by several misconfigurations in the way the connection was managed.

## Timeline

10:00 AM PST: Our monitoring system noted that database queries were suddenly taking longer to get a response.
10:10 AM PST: Our engineers noticed an increase in error reports and a slowdown in the web app.
10:30 AM PST: We investigated the issue and found that queries were piling up in the database.
11:45 AM PST: Upon investigation, the connection settings were changed and the problem was resolved.

## Root Cause and Solution.
The database was stuck because of the way the connection was being handled, which was resolved by adjusting the settings and optimizing the way queries were executed.
Corrective and Preventive Actions

## Improvement/Fix:
Review and properly adjust database connection settings.
Set up better monitoring to detect deadlock issues before they become failures.
Regularly check and fine-tune the way queries are executed to improve performance.
## Tasks
Update database connection settings.
Create a tool to automatically monitor deadlock conditions.
Perform periodic performance checks of database operations.
