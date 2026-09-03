# CareLens — Architecture

## 1. Initial Architecture

The initial CareLens backend is implemented as a Python FastAPI application.

```text
Client
  |
  | HTTP
  v
FastAPI Application
  |
  +-- API Routes
  |
  +-- Services
  |
  +-- Repositories
  |
  +-- Models
  |
  +-- Schemas
```

The project uses a layered architecture so that API routing, business logic, database access, and data models remain separated.

## 2. Backend Components

### API Layer

Responsible for:

- HTTP endpoints
- Request handling
- Response handling
- API versioning

Current API prefix:

`/api/v1`

### Service Layer

Responsible for:

- Business logic
- Application workflows
- Data processing

The service layer will be introduced as business functionality is implemented.

### Repository Layer

Responsible for:

- Database access
- Query execution
- Persistence operations

The repository layer will be implemented when PostgreSQL is introduced.

### Model Layer

Responsible for:

- Database models
- Domain entities

### Schema Layer

Responsible for:

- Request validation
- Response serialization
- API contracts

Pydantic will be used for API schemas.

## 3. Current API

### GET /api/v1/health

Returns the health status of the API service.

Example response:

```json
{
  "status": "healthy",
  "service": "CareLens API",
  "version": "0.1.0",
  "environment": "development"
}
```

## 4. API Documentation

FastAPI automatically generates:

- Swagger UI at `/docs`
- ReDoc at `/redoc`

## 5. Containerization

The backend is packaged as a Docker image using `python:3.12-slim`.

The container exposes port `8000`.

## 6. Future Architecture

The backend will eventually integrate with:

- PostgreSQL / Cloud SQL
- Firestore
- Firebase Authentication
- Google Cloud Storage
- AI services
- Cloud Run

````

---

# 2.15 Update the development log

Add this to:

```text
docs/10-development-log.md
````

## 2026-09-02 — Step 2: FastAPI Backend Foundation

### Completed

- Created the FastAPI backend structure.
- Created a Python virtual environment.
- Added FastAPI and supporting dependencies.
- Implemented centralized application configuration.
- Implemented API versioning using `/api/v1`.
- Added the initial root endpoint.
- Added the health-check endpoint.
- Enabled automatic Swagger and ReDoc documentation.
- Added the first automated API test.
- Containerized the FastAPI backend using Docker.

### Endpoints

- `GET /`
- `GET /api/v1/health`

### Testing

The health endpoint is covered by an automated Pytest test.

### Current Architecture

```text
Client
   |
   v
FastAPI
   |
   +-- API
   +-- Services
   +-- Repositories
   +-- Models
   +-- Schemas
```

### Next Step

Introduce PostgreSQL and SQLAlchemy, establish the database connection, and design the initial CareLens data model.
