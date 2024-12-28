# theatre_api
API service for theater

## Description

Theatre API is a web application for managing a theatre, allowing users to view and manage performances, book tickets, and administer schedules. The application features user authentication, permission management, and administrative functionalities for handling theatre-related operations.

## Table of Contents

### Technologies
### Installation and Setup
### Using Docker
### Running Tests
### API Documentation
### Using the Application
### Authorization and Authentication
## Technologies
### Django - the main web framework.
### Django REST Framework - used for building the API.
### SQLite - the database for development; can be replaced with PostgreSQL for production.
### Django JWT - for user authentication using JSON Web Tokens.
### Pillow - for image handling.

## Installation and Setup
Clone the repository:
git clone https://github.com/OlhaStadnik/theatre_api.git
cd theatre_api
Create and activate a virtual environment:
python -m venv venv
### For Windows
venv\Scripts\activate
### For MacOS/Linux
source venv/bin/activate
Install the required packages:
pip install -r requirements.txt
### Set up the database:
For development, SQLite is already configured.
For production, replace the database configuration in settings.py with PostgreSQL credentials.
Run migrations:
python manage.py migrate
Create a superuser (optional):
python manage.py createsuperuser
Run the server:
python manage.py runserver

## Using Docker
If you prefer to use Docker for setting up the project, follow these steps:
Ensure Docker and Docker Compose are installed.
Build and run the containers:
docker-compose up --build
Access the application at:
http://localhost:8000
Run migrations within the Docker container (if needed):
docker-compose exec app python manage.py migrate
Create a superuser in the Docker container (optional):
docker-compose exec app python manage.py createsuperuser

## Running Tests
python manage.py test

## API Documentation
The Theatre API provides endpoints for managing performances, users, and permissions. Below are some key endpoints:

User Registration: POST /api/user/register/
Token Obtain: POST /api/user/token/
Token Refresh: POST /api/user/token/refresh/
Get Current User: GET /api/user/me/

##
Using the Application
Visit http://localhost:8000 to access the application.
You can register as a user and log in to book performances and view details.
Admin users can manage performances, schedules, and other content via the admin panel.

## Authorization and Authentication
This application uses JWT (JSON Web Tokens) for user authentication. Users must log in to access certain features. After successful login, users will receive a token that must be included in the headers of subsequent requests:
http
Authorization: Bearer <your_token>
