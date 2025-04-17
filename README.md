# Dockerized SQL Server & Pytest Automation

This project demonstrates how to set up a containerized SQL Server environment with Docker and test it using pytest. The tests validate the addition logic in test data stored in SQL Server. Additionally, the setup includes automation to install dependencies and execute tests in the test runner container.

## Project Structure

```
jenkins-pytest-sql
├── docker-compose.yml         # Defines two containers for the project - SQL Server and pytest runner
├── Dockerfile.sqlserver       # SQL Server container build configuration
├── init-data.sql              # SQL script to initialize test data in SQL Server
├── requirements.txt           # Python dependencies for pytest and pymssql
├── tests/                     # Directory containing a pytest
│   └── test_db.py             # Pytest file to test addition logic
└── .env                       # Environment variables for containerized services
```


## Installation & Usage

### 1. Clone the repository and cd to the directory

```
cd jenkins-pytest-sql
```
### 2. Configure environment variables
Create a .env file in the root directory (if not already present), and set the SA password:

```
MYSQL_SA_PASSWORD=YourStrongPassword123!
```
### 3. Build and run the containers
```
docker-compose up --build
```
This command will 
- build the SQL Server container and run the init-data.sql script to insert test data.

- build the test-runner container, install Python dependencies, and run the pytest suite.

### 4. Check test results
Test results will be displayed in the Docker logs of the test-runner container. You can also view them in Docker Desktop under the Logs tab for test-runner.