# MySQL


# Tasks To Complete

### 0. Install MySQL

Install MySQL on your web-01 and web-02 servers.
Make sure that task #3 of your SSH project is completed for web-01 and web-02. The checker will connect to your servers to check MySQL status.
### 1. Let us in!

Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost

### 2. If only you could see what I've seen with your eyes

Create a database named tyrell_corp.
Within the tyrell_corp database create a table named nexus6 and add at least one entry to it. This is needed 
### 3. Quite an experience to live in fear, isn't it?

The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.

### 4. Setup a Primary-Replica infrastructure using MySQL

MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter
MySQL replica must be hosted on web-02.

### 5. MySQL backup

### 5-mysql_backup contains a Bash script that generates a MySQL dump and creates a compressed archive out of it.

The MySQL dump must contain all your MySQL databases.
