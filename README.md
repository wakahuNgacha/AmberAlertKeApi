# AmberAlertKeApi

AmberAlertKeApi is a Django REST Framework API for managing user accounts, reporting missing persons, and tracking anonymous/registered alerts for a missing-person response workflow.

## Project purpose

The API exposes a small service for:

- registering and authenticating users
- creating and managing missing-person records
- submitting reports tied to a user and a missing person
- exposing protected endpoints through JWT authentication

## Tech stack

- Python 3.11+
- Django 5.1.5
- Django REST Framework 3.15.2
- djangorestframework-simplejwt
- PostgreSQL (configured by default)
- Pillow for image handling

## Repository layout

```text
AmberAlertKeApi/
├── Api/
│   ├── Api/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── missingPerson/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── report/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   └── user/
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

## Application modules

### `user`

Handles user registration, authentication, and profile listing.

Key behaviors:

- `POST /register/` creates a new user
- `POST /login/` issues JWT tokens
- `POST /token/refresh/` refreshes an access token
- `GET /users/` lists users
- `GET /users/<id>/` retrieves one user
- `PUT /users/<id>/` updates a user
- `DELETE /users/<id>/` removes a user

### `missingPerson`

Stores a recorded missing person and exposes CRUD routes.

- `GET /missing-persons/` lists records
- `GET /missing-persons/<id>/` retrieves one record
- `POST /missing-persons/` creates a new record
- `PUT /missing-persons/<id>/` updates a record
- `DELETE /missing-persons/<id>/` deletes a record

### `report`

Links a report to a `User` and a `MissingPerson` entry.

- `GET /reports/` lists reports
- `GET /reports/<id>/` retrieves one report
- `POST /reports/` creates a new report
- `PUT /reports/<id>/` updates a report
- `DELETE /reports/<id>/` deletes a report

## Authentication

The API uses JWT via `djangorestframework_simplejwt`.

The project config sets:

- `DEFAULT_AUTHENTICATION_CLASSES` to `JWTAuthentication`
- `DEFAULT_PERMISSION_CLASSES` to `IsAuthenticated`

This means most endpoints are protected unless the view explicitly allows public access. The `register` and `login` endpoints are intentionally public.

## Local setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a PostgreSQL database and user for the project.

```sql
CREATE DATABASE amberalertke;
CREATE USER amberalertke_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE amberalertke TO amberalertke_user;
```

4. Create an environment file.

Create a `.env` file in the project root (same directory as `README.md`) or export the variables in your shell. The project expects the following variables:

```env
DATABASE_NAME=amberalertke
DATABASE_USER=amberalertke_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

A sample is available in `.env.example` in the repository root.

5. Apply migrations.

From the `Api/` directory:

```bash
cd Api
python manage.py migrate
```

6. Create a superuser if needed.

```bash
python manage.py createsuperuser
```

7. Run the development server.

```bash
python manage.py runserver
```

The app will be available at:

- `http://127.0.0.1:8000/`

## Notes on configuration

- `Api/Api/settings.py` is configured for PostgreSQL and reads database values from environment variables using `python-decouple`.
- `SECRET_KEY` is currently hard-coded in development settings. For production, replace it with an environment-managed secret.
- `DEBUG` is also currently enabled; disable it in production.

## Example payloads

### Register a user

```json
{
  "email": "user@example.com",
  "firstName": "Jane",
  "secondName": "Achieng",
  "surname": "Mwangi",
  "location": "Nairobi",
  "password": "StrongPass123!",
  "password_confirm": "StrongPass123!"
}
```

### Login

```json
{
  "email": "user@example.com",
  "password": "StrongPass123!"
}
```

### Create a missing person

```json
{
  "firstName": "John",
  "secondName": "Otieno",
  "surname": "Kamau",
  "gender": "male",
  "description": "Last seen near Nairobi CBD wearing a blue jacket.",
  "image": "images/example.jpg",
  "status": "missing"
}
```

### Create a report

```json
{
  "user": 1,
  "missingPerson": 1,
  "message": "I believe this person was last seen in Kawangware."
}
```

## Development guidance

- Keep all environment-specific values outside the source control tree.
- Use migrations for any schema changes.
- Use a fresh PostgreSQL database for local development to match production behavior.
- Protect sensitive secrets and avoid committing `.env` files.

## License

This project is distributed under the MIT license. See [LICENSE](LICENSE) for details.
