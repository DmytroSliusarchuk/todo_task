# Django REST Framework Todo API 

## Project overview
This project is a Django REST Framework API that provides functionalities for creating, updating, getting, deleting and marked as completed todos. Also it provides an interactive API documentation using drf-yasg and Swagger UI.

## Features

* Todos Management
    * Create, retrieve, update, and delete todos.
    * Mark todos as completed.
* API Documentation
    * Interactive API documentation using drf-yasg, Swagger UI

## Prerequisites

* Python 3.10+

## Installation

1. Clone the repository
```bash
git clone https://github.com/DmytroSliusarchuk/todo_task.git
cd todo_task
```

2. Create a virtual environment and activate it
```bash
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```
Update the `.env` file with your settings.

5. Run migrations
```bash
python manage.py migrate
```

6. Start the Django development server
```bash
python manage.py runserver
```

## API Documentation

Access the interactive API documentation at:

- Swagger UI: http://localhost:8000/swagger/

## Environment Variables

Ensure the following environment variables are set:

- DJANGO_SECRET_KEY: Django secret key
