# task2

PROBLEM STATEMENT

DESCRIPTION OF THE TASK PROCESS

1. Create a container image that’s has Jenkins installed using Dockerfile.

2. When we launch this image, it should automatically start the Jenkins service in the container.

3. Create a job chain of job1, job2, job3, job4, and job5 using the build pipeline plugin in Jenkins.

Job1: Pull the Github repo automatically when some developers push the repo to Github.

Job2: By looking at the code or program file, Jenkins should automatically start the respective language interpreter; install image container to deploy code ( eg. If code is of PHP, then Jenkins should start the container that has PHP already installed ).

Job3: Test your app if it is working or not.

Job4: If the app is not working, then send an email to the developer with error messages.

Job5: Create this extra job for monitor. If this container where the app is running fails due to any reason then this job should automatically re-start the container.

DETAILED SOLUTION 

https://snehakothavenkat.blogspot.com/2020/07/integration-of-git-jenkins-and-docker.html
