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

4. Healthcare Domain Model

The initial healthcare domain consists of six relational entities:

Organizations
Members
Providers
Procedures
Claims
Claim lines
Organizations

Represents a healthcare organization using the CareLens platform.

An organization can have multiple members and providers.

Members

Represents individuals whose healthcare activity is being analyzed.

Each member belongs to an organization and can have multiple claims.

Important fields include:

Member number
First name
Last name
Date of birth
Organization
Providers

Represents healthcare providers or provider organizations.

Each provider belongs to an organization and can be associated with multiple claims.

Important fields include:

Provider number
Name
Specialty
Organization
Procedures

Represents healthcare services identified by procedure codes.

Important fields include:

Procedure code
Description
Claims

Represents a healthcare billing event.

A claim belongs to:

One member
One provider

A claim can contain multiple claim lines.

Important fields include:

Claim number
Member
Provider
Service date
Total amount
Status
Claim Lines

Represents individual services contained within a claim.

Each claim line belongs to:

One claim
One procedure

Important fields include:

Claim
Procedure
Quantity
Amount 5. Relationships

The current relationship model is:

Organization
|
+----< Members
|
+----< Providers

Member
|
+----< Claims

Provider
|
+----< Claims

Claim
|
+----< Claim Lines

Procedure
|
+----< Claim Lines

The notation ----< represents a one-to-many relationship.

6. Indexing Strategy

Indexes have been added to fields frequently used for:

Lookups
Foreign-key joins
Filtering
Claim analytics

Current indexed fields include:

Member number
Provider number
Procedure code
Organization foreign keys
Member foreign keys
Provider foreign keys
Claim number
Claim service date
Claim line foreign keys

The indexing strategy will be reviewed as query patterns are introduced.

7. Data Integrity

The database uses:

Primary keys
Foreign keys
Non-null constraints
Unique constraints
Numeric precision for monetary values

Healthcare monetary amounts use PostgreSQL NUMERIC(12, 2) rather than floating-point types to avoid monetary precision problems.

8. Migration

The healthcare domain schema is managed using Alembic.

The migration workflow is:

SQLAlchemy Model
|
v
Alembic Autogenerate
|
v
Migration Review
|
v
alembic upgrade head
|
v
PostgreSQL
