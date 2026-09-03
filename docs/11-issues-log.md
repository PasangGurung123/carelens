Incident Log: PostgreSQL “role does not exist” Blocking API Database Connection
Date: 2026-09-03
Environment: Local development (macOS, Homebrew PostgreSQL)
Component: CareLens API – database connectivity (SQLAlchemy + psycopg)
Reported by: Developer
Resolved by: Developer

1. Summary
   The CareLens API could not connect to the local PostgreSQL database. Tests and manual connections failed with:

psql: error: connection to server at "localhost" (::1), port 5432 failed: FATAL: role "carelens" does not exist

Root cause: the PostgreSQL cluster had no role (user) named carelens, which the application’s connection string required. The issue was resolved by creating the missing role and database, then granting appropriate privileges.

2. Symptoms
   Running the test:

python
def test_database_connection():
with engine.connect() as connection:
result = connection.execute(text("SELECT 1"))
assert result.scalar() == 1
raised an exception inside SQLAlchemy when calling engine.raw_connection().

Direct psql connection using the same credentials failed:

bash
psql "postgresql://carelens:carelens_dev_password@localhost:5432/carelens"

# psql: error: ... FATAL: role "carelens" does not exist

PostgreSQL was running and reachable; only authentication/role configuration was incorrect.

3. Impact
   Local development environment non-functional for any feature requiring database access.

Blocked:

API startup tests

Database migration runs (Alembic)

Any integration tests relying on engine.connect()

No production impact (issue confined to local dev).

4. Root Cause Analysis
   What happened:
   The application configuration (config.py) defined:

python
database_url: str = (
"postgresql+psycopg://"
"carelens:carelens_dev_password@"
"localhost:5432/carelens"
)
This expects:

A PostgreSQL role named carelens with LOGIN privilege

A database named carelens

Password authentication with carelens_dev_password

On this machine, PostgreSQL was installed via Homebrew with a superuser role pasanggurung, but no carelens role or carelens database existed. Therefore, any connection attempt using that role failed with:

FATAL: role "carelens" does not exist

Why it happened:

Initial PostgreSQL setup created only the OS-mapped superuser (pasanggurung).

No migration or setup script created the application role/database.

Configuration assumed these objects already existed.

5. Resolution Steps
   All commands were executed on the developer’s local machine.

5.1. Confirm existing roles
bash
psql -h localhost -p 5432 -d postgres -c '\du'
Output showed only:

text
Role name | Attributes
--------------+------------------------------------------------------------
pasanggurung | Superuser, Create role, Create DB, Replication, Bypass RLS
No carelens role existed.

5.2. Connect as superuser
bash
psql -h localhost -p 5432 -U pasanggurung -d postgres
5.3. Create application role and database
Inside psql:

sql
-- Create login role for the application
CREATE ROLE carelens WITH LOGIN PASSWORD 'carelens_dev_password';

-- Create the database owned by that role
CREATE DATABASE carelens OWNER carelens;

-- Grant database-level privileges
GRANT ALL PRIVILEGES ON DATABASE carelens TO carelens;

-- Switch to the new database
\c carelens;

-- Grant schema and object privileges
GRANT ALL ON SCHEMA public TO carelens;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO carelens;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO carelens;

-- Set default privileges for future objects
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO carelens;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO carelens;
Then exit:

sql
\q
These steps ensure the carelens role can connect, use the public schema, and fully manage tables/sequences created in the carelens database.

5.4. Verify connection
bash
psql "postgresql://carelens:carelens_dev_password@localhost:5432/carelens"
Connection succeeded without errors.

Python test then passed:

python
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg://carelens:carelens_dev_password@localhost:5432/carelens"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
result = conn.execute(text("SELECT 1"))
assert result.scalar() == 1 # passes 6. Lessons Learned
Database bootstrap is part of setup
Installing PostgreSQL is not enough; application-specific roles and databases must be created before the app can connect.

Use psql to validate connection strings early
Testing the exact connection URL with psql quickly isolates whether an issue is in PostgreSQL configuration vs. application code.

Document local dev bootstrap steps
New developers (or new machines) will hit the same issue unless role/database creation is documented or automated.

7. Preventive Actions
   To avoid recurrence:

Add a setup script (e.g. scripts/setup_local_db.sql or a Makefile target) that:

Creates the carelens role if it doesn’t exist

Creates the carelens database if it doesn’t exist

Grants required privileges

Update onboarding / README with a “Local Database Setup” section, including:

bash

# Example (to be adapted to your environment)

psql -h localhost -p 5432 -U <your_superuser> -d postgres -f scripts/setup_local_db.sql
Consider environment-driven URLs
Keep DATABASE_URL in .env and document required DB objects, so mismatches between config and actual DB state are obvious during setup.

8. References
   PostgreSQL role/permission management: CREATE ROLE, GRANT, ALTER DEFAULT PRIVILEGES

Common pattern for “role does not exist” errors and fixes

Best practices for incident/resolution documentation

Status: Resolved
Next steps:

Add DB bootstrap script and update project README with local setup instructions.

Optionally automate role/database creation in CI or dev container initialization.
