# HealthApp

## Description

HealthApp is a secure health management application designed specifically for healthcare organizations. Effective cybersecurity measures are essential to protect sensitive patient information. This software application is developed through research on cybersecurity in healthcare, to emphasizes the importance of prioritizing cybersecurity within the healthcare industry. The application addresses the critical need for robust security measures to safeguard patient data and ensure uncomprmised patient care.

## Technologies

HealthApp is build using Django which is a web framework for scalable and secure development, PostgreSQL for secure database management, HTML for user interface design, Docker container specifically for PostgreSQL database for setup process and scalability.

## Features

Some of the key features of this application are:

- Input validation: On login credentials, adding, and modifying data. Any input is validated for data integrity and to prevent injection attacks.
- Two factor authentication: This security feature along wit input credentials help prevent unauthorozed access (use google authenticator to setup).
- Cryptographic technique: Using cryptographic techniques for communication wheather across networks or within the database it helps protecting patients data from tampering. In this application passwords stored hashed.
- Auto session logout: Automatic session logout terminates user sessions after 5 minutes of inactivity, reducing the risk of unauthorized access.
- Data normalization: This ensures consistency and integrity within the database reducing redundancy.
- Audit logging: All activities such as modificatio, additions made to the models and data accessed within the application is tracked and recorded in the database. This feature provides an audit trail for compliance with HIPAA and for security purposes.

## Prerequisites

- Docker installed on your machine ([installation guide](https://docs.docker.com/get-docker/))
- Python 3.11.4 installed on your machine
- PostgreSQL client (for database management)

## Installation

1. Clone the repository:

   ```bash
   git clone <this reposi>
   cd <repository_name>

2. Setting up the virtual environment

    ```bash
    # Navigate to the project directory
    cd webapp

    # Activate the virtual environment
    source .venv/bin/activate

3. Start PostgreSQL Docker container

   ```bash
   docker run --hostname=f27aa69539ee \
           --env=POSTGRES_PASSWORD=root \
           --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/16/bin \
           --env=GOSU_VERSION=1.16 \
           --env=LANG=en_US.utf8 \
           --env=PG_MAJOR=16 \
           --env=PG_VERSION=16.0-1.pgdg120+1 \
           --env=PGDATA=/var/lib/postgresql/data \
           --volume=/var/lib/postgresql/data \
           -p 2022:5432 \
           --restart=no \
           --runtime=runc \
           -d postgres

4. Dependencies: (I reccoment using pycharm for automatic suggestions of dependencies to install)

   ```bash
   pip install -r requirement.txt

5. Migrations if necessary:

   ```bash
   python manage.py migrate

## Usage

1. Make sure you are in 'webapp' folder:

    ```bash
    cd webapp

2. If using Docker make sure you start the container (if not skip to 3)
3. Run the Django server

   ```bash
   python manage.py runserver

4. Access the application in your browser at <http://localhost:8000>

## Additional Notes

- If you need to access the PostgreSQL database from your local machine, you can use the following command:

    ```bash
    psql -h localhost -p 2022 -U postgres

Replace 2022 with the appropriate port if you have configured it differently and make sure to change it in the settings database configuration to however you configured your database.

- Deactivate and stop container when done
  