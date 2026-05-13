# FastAPI User Management API

A simple FastAPI CRUD project with MySQL database integration, image upload handling, validation, and Alembic migrations.

---

## Features

- User CRUD Operations
- Image Upload and Local Storage
- Image Replace on Update
- Image Delete on User Delete
- Email Validation
- Duplicate Email Checking
- Gender Enum Validation
- HTTP Exception Handling
- Alembic Database Migrations

---

## Technologies Used

- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- Pydantic

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/user` | Create User |
| GET | `/user` | Get All Users |
| PUT | `/user/{user_id}` | Update User |
| DELETE | `/user/{user_id}` | Delete User |

---

## Setup

### Install Requirements

```bash
pip install -r requirements.txt
```

### Create `.env`

```env
DATABASE_URL=your_database_url
```

### Run Migration

```bash
alembic upgrade head
```

### Run Server

```bash
uvicorn app.main:app --reload
```

---

## Swagger Documentation

```txt
http://127.0.0.1:8000/docs
```
