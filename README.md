# FastAPI_task_management_app
A FastAPI-based backend project developed from scratch while learning and implementing core FastAPI concepts. The project includes essential backend features such as RESTful APIs, database integration, authentication, migrations, email functionality, and structured project architecture. Every component was implemented step by step.

FastAPI Task Management App

A backend REST API built with FastAPI from scratch as part of my FastAPI learning journey. The project was developed step by step while learning and implementing core backend concepts such as RESTful API development, authentication, database integration, migrations, password security, environment configuration, and email functionality.

The goal of this project was not only to build a task management application, but also to understand how a production-style FastAPI backend is structured and how its different components work together.

🚀 Features

FastAPI REST APIs for building the backend

Task management functionality through API endpoints

User registration and authentication

JWT-based authentication

Password hashing for securely storing user passwords

PostgreSQL database integration

SQLAlchemy for database interaction

Alembic for database migrations

Pydantic models for request validation and structured data

Email functionality using FastAPI Mail and Gmail SMTP

Environment variables using .env for sensitive configuration

Automatic API documentation through FastAPI Swagger UI

Postman support for testing API requests

Organized backend structure using separate application modules

🛠️ Technologies Used

Technology

Purpose

Python

Backend programming language

FastAPI

Web framework for building REST APIs

Pydantic

Data validation and request/response schemas

SQLAlchemy

ORM and database interaction

PostgreSQL

Relational database

Alembic

Database schema migrations

JWT

Authentication and authorization

Passlib / password hashing

Secure password handling

FastAPI Mail

Sending emails

Gmail SMTP

Email delivery

python-dotenv

Loading environment variables

Uvicorn

ASGI server

Postman

API testing

Git & GitHub

Version control and project hosting

📁 Project Structure

FastAPI_task_management_app/
│
├── migration/              # Alembic migration files
│
├── src/                    # Main application source code
│   └── ...                 # Application modules
│
├── main.py                 # FastAPI application entry point
├── alembic.ini             # Alembic configuration
├── requirement.txt         # Python dependencies
├── .gitignore              # Files excluded from Git
├── .env                    # Local environment variables (not committed)
└── README.md               # Project documentation

The exact modules inside src/ may vary as the project evolves. The application code is separated from the root configuration files to keep the project organized.

⚙️ Getting Started

1. Clone the repository

git clone https://github.com/Ankit-2404/FastAPI_task_management_app.git

Move into the project directory:

cd FastAPI_task_management_app

2. Create a virtual environment

Windows:

python -m venv .venv

Activate it in PowerShell:

.venv\Scripts\Activate.ps1

Or in Git Bash:

source .venv/Scripts/activate

3. Install dependencies

pip install -r requirement.txt

🔐 Environment Variables

Create a .env file in the project root.

The project uses environment variables for sensitive values such as database credentials, JWT configuration, and email credentials.

A typical configuration can look like:

DATABASE_URL=your_database_connection_string

SECRET_KEY=your_secret_key

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_gmail_app_password
MAIL_FROM=your_email@gmail.com

Never commit your real .env file or passwords/API secrets to GitHub.

The repository's .gitignore should keep .env and the virtual environment out of version control.

🗄️ Database & Migrations

This project uses PostgreSQL as the database and SQLAlchemy for database operations.

Alembic is used to manage database schema changes.

After configuring the database, migrations can be managed with commands such as:

alembic upgrade head

When a model/database change needs a new migration:

alembic revision --autogenerate -m "describe your change"

Then apply the migration:

alembic upgrade head

▶️ Running the Application

Start the FastAPI application with Uvicorn:

uvicorn main:app --reload

The API will normally be available at:

http://127.0.0.1:8000

📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI

http://127.0.0.1:8000/docs

ReDoc

http://127.0.0.1:8000/redoc

Swagger UI can be used to understand and manually test the available API endpoints.

🔑 Authentication Flow

The authentication system follows a typical API authentication flow:

User Registration
       ↓
Password Hashing
       ↓
User Stored in PostgreSQL
       ↓
User Login
       ↓
Credentials Verified
       ↓
JWT Token Generated
       ↓
Token Sent with Protected Requests
       ↓
JWT Validated
       ↓
Authorized API Access

Passwords are not intended to be stored as plain text. The application hashes passwords before storing them in the database.

JWT tokens are used to authenticate requests to protected resources.

📧 Email Functionality

The application includes registration-related email functionality using FastAPI Mail.

The email configuration is kept outside the source code through environment variables, while Gmail's SMTP server is used to deliver messages.

The basic flow is:

Registration
     ↓
Application creates email message
     ↓
FastAPI Mail
     ↓
Gmail SMTP
     ↓
Recipient's Inbox

🧪 API Testing

The APIs can be tested using:

FastAPI Swagger UI

Postman

Postman is useful for testing HTTP methods such as:

GET
POST
PUT
DELETE

and for testing authenticated requests by sending the JWT token with protected API calls.

🧠 What I Learned

This project was created as a practical way to understand FastAPI and backend development rather than simply following isolated tutorials.

During the development process, I worked with concepts including:

Creating and organizing a FastAPI application

REST API design

HTTP methods and status codes

Request and response handling

Pydantic validation

Dependency-based application design

SQLAlchemy and ORM concepts

PostgreSQL database connectivity

Database models and relationships

Alembic migrations

User registration and login

Password hashing

JWT authentication

Protected API endpoints

Environment variables and .env

SMTP email integration

API testing with Postman

Interactive API documentation with Swagger

Git and GitHub version control

🔒 Security Considerations

Sensitive configuration should be stored in environment variables rather than directly in the source code.

The following should not be committed to GitHub:

.env
.venv/
__pycache__/
*.pyc

In particular, never expose:

Database passwords

Gmail/App Passwords

JWT secret keys

Other private credentials

🎯 Project Purpose

This project represents my progression through learning FastAPI backend development.

I built the application step by step from scratch while learning the underlying concepts. The code in this repository was written and implemented by me during that learning process, with the focus on understanding how each part of a FastAPI backend works and how the components fit together.

👨‍💻 Author

Ankit Singh

B.Tech Computer Science
Poornima University, Jaipur

GitHub: Ankit-2404

⭐ If you find this project useful, feel free to explore the code and give the repository a star.
