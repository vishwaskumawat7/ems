# Employee Management System - EMS

## Run the application

1. Creating Virtual Env and Installing the requirements:

    - Create virtual environmnt using this command: `python3 -m venv env`
    - Activate it using: `. env/bin/activate`
    - Install the requirements: `pip install -r requirements.txt`

2. Create `.env` file to store the database related variables. You can refer `.env.example` file for reference

3. Install the PostgreSQL and then create a database

    - Update the package and install the PostgreSQL:  
            
        - `sudo apt update`

        - `sudo apt install postgresql postgresql-contrib`

    - We have installed a psycopg2 driver which will help Django to talk with PostgreSQL.
    - Switching to the Postgres user: `sudo -i -u postgres`
    - Open the Postgre shell - `psql`
    - In the shell, we will run following commands to create a database and a user-

            -- Create a new database myproject
            CREATE DATABASE database_name;

            -- Create a user with password
            CREATE USER username WITH PASSWORD 'password';

            -- Connect with the database
            \c database_name 

            -- Give access
            GRANT ALL ON SCHEMA public TO username;

            -- Giving permission to user to create databases (It will be helpful when testing our app)
            ALTER USER username CREATEDB;

            -- exit shell
            \q  
            
    - Exit the PostgreSQL Environment using `ctrl+d`.

    - Creating database tables:
    `python3 manage.py migrate`

4. Run the application: `python3 manage.py runserver`


## Test the application

Some of the test cases are written under ems/tests.py file.

Run Tests: `python3 manage.py test`