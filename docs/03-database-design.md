# CareLens — Database Design

## 1. Database Technology

CareLens uses PostgreSQL as its primary relational database.

PostgreSQL will store structured healthcare and analytical data such as:

- Organizations
- Members
- Providers
- Claims
- Claim lines
- Procedures
- Diagnoses

The production deployment will use Google Cloud SQL for PostgreSQL.

## 2. Database Access

The FastAPI backend uses SQLAlchemy as its ORM and database abstraction layer.

The application uses:

- SQLAlchemy
- psycopg
- Alembic

SQLAlchemy manages database connections and sessions, while Alembic manages schema migrations.

## 3. Initial Entity

### Organizations

An organization represents a healthcare organization using the CareLens platform.

Current fields:

| Column     | Type        | Constraints                  |
| ---------- | ----------- | ---------------------------- |
| id         | Integer     | Primary key                  |
| name       | String(255) | Required                     |
| created_at | Timestamp   | Required, database-generated |

## 4. Initial Relationship Model

The planned data model is:

```text
Organization
     |
     +----------------+
     |                |
     v                v
  Members          Providers
     |
     v
  Claims
     |
     v
Claim Lines
```

The complete relationship model will be introduced incrementally.

## 5. Migration Strategy

Database schema changes are managed through Alembic migrations.

The development workflow is:

```text
Modify SQLAlchemy model
        |
        v
Generate migration
        |
        v
Inspect migration
        |
        v
Apply migration
        |
        v
Verify database
```

Migrations will be committed to Git so that database schema changes are version-controlled alongside application code.

## 6. Local Development Database

Local development uses PostgreSQL through Docker Compose.

Database configuration:

- Database: `carelens`
- User: `carelens`
- Port: `5432`

Development credentials are local-only and must not be used in production.

Production credentials will be managed through Google Cloud's secret-management facilities rather than committed to source control.
