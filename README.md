# Automation API with FastAPI

A modern task management API built with FastAPI that allows users to organize and track their daily tasks. Features include user authentication with JWT tokens, complete CRUD operations for tasks, and filtering by date and priority.

## 🎯 Project Motivation

This project was built to practice and demonstrate real-world backend concepts
such as authentication, authorization, persistence, and clean API design using FastAPI.

## 🚀 What the API Does

This API provides a complete task management system where users can:
- **Register and authenticate** securely with JWT tokens
- **Create tasks** with title, description, date, and priority (low/medium/high)
- **List tasks** with optional filtering by date
- **Update tasks** including status (pending/in_progress/done) and other fields
- **Delete tasks** when they're no longer needed
- All tasks are **user-specific** - users can only access their own tasks

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLModel** - SQL database library with type hints (combines SQLAlchemy + Pydantic)
- **Python-JOSE** - JWT token implementation for authentication
- **Passlib + Bcrypt** - Password hashing and verification
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI server for running the application
- **Poetry** - Dependency management and packaging

## 🚧 Future Improvements

- Refresh token implementation
- Role-based access control (RBAC)
- Task recurrence (daily / weekly)
- Pagination and sorting for task lists
- Background jobs for reminders
- Frontend integration (React or mobile client)


## 🔐 Authentication Flow

### 1. Register a New User
```bash
POST /auth/register
{
  "email": "user@example.com",
  "password": "securepassword"
}
```
Response: User details (without password)

### 2. Login to Get Token
```bash
POST /auth/login
{
  "email": "user@example.com",
  "password": "securepassword"
}
```
Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### 3. Access Protected Routes
Include the token in the Authorization header:
```bash
GET /tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

All `/tasks` endpoints are protected and require a valid JWT token. The API automatically:
- Validates the token
- Extracts the user ID
- Ensures users can only access their own tasks

## 📦 How to Run Locally

### Prerequisites
- Python 3.13+
- Poetry (for dependency management)

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd automation-api-fastapi
```

2. **Install dependencies**
```bash
poetry install
```

3. **Create a `.env` file** (optional, for custom configuration)
```bash
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DEBUG=True
```

4. **Run the application**
```bash
poetry run uvicorn app.api.app:app --reload
```

The API will be available at `http://localhost:8000`

5. **Access the interactive API documentation**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📚 API Endpoints

### Authentication
- `POST /auth/register` - Create a new user account
- `POST /auth/login` - Login and receive JWT token

### Tasks (All require authentication)
- `POST /tasks` - Create a new task
- `GET /tasks` - List all tasks (optional `?task_date=2024-01-15` filter)
- `GET /tasks/{task_id}` - Get a specific task
- `PATCH /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

### Health Check
- `GET /` - Basic health check endpoint

## 💡 Example Usage

1. **Register a user:**
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "mypassword"}'
```

2. **Login and get token:**
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "mypassword"}'
```

3. **Create a task:**
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README",
    "date": "2024-01-15",
    "priority": "high"
  }'
```

4. **List all tasks:**
```bash
curl -X GET http://localhost:8000/tasks \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## 🗂️ Project Structure

```
automation-api-fastapi/
├── app/
│   ├── api/
│   │   ├── routes/         # API route handlers
│   │   ├── dependencies.py # Shared dependencies (auth)
│   │   └── app.py          # FastAPI app initialization
│   ├── core/
│   │   ├── config.py       # App settings and configuration
│   │   ├── database.py     # Database connection
│   │   └── security.py     # Password & JWT utilities
│   ├── models/             # SQLModel database models
│   ├── services/           # Business logic layer
│   └── storage/            # Data persistence layer
├── tests/                  # Test files
├── pyproject.toml          # Poetry dependencies
└── README.md
```

## 🔧 Configuration

The application can be configured via environment variables or a `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Secret key for JWT signing | `CHANGE_ME` |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | `60` |
| `DEBUG` | Enable debug mode | `True` |
| `APP_NAME` | Application name | `Automation API` |

**⚠️ Important:** Change the `SECRET_KEY` in production!

## 📄 License

This project is open source and available for educational purposes.


