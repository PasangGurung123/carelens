# CareLens — Project Overview

## 1. Introduction

CareLens is an AI-powered healthcare analytics platform designed to demonstrate production-grade full-stack software engineering, data engineering, cloud deployment, and AI-assisted application development.

The platform ingests healthcare claims-like data, validates and transforms the data through an ETL pipeline, stores analytical data in PostgreSQL, exposes analytics through a Python/FastAPI backend, and presents the results through a React and TypeScript web application.

The platform will also incorporate Firebase Authentication, Firestore, Google Cloud services, and an AI-powered natural-language analytics assistant.

## 2. Problem Statement

Healthcare organizations generate large volumes of claims, member, provider, procedure, and cost data.

Raw healthcare data is difficult to use directly because it may contain:

- Missing values
- Duplicate records
- Invalid dates
- Invalid identifiers
- Inconsistent data formats
- Incorrect or invalid monetary values

CareLens addresses these challenges by providing a pipeline for data ingestion, validation, transformation, storage, and analytics.

The platform allows authorized users to explore healthcare cost and utilization information through dashboards and natural-language questions.

## 3. Objectives

The primary objectives are:

1. Build a production-style backend using Python and FastAPI.
2. Build a modern frontend using React and TypeScript.
3. Implement an automated ETL pipeline using Python.
4. Demonstrate advanced SQL using PostgreSQL.
5. Use Firestore for document-oriented application data.
6. Implement authentication and role-based authorization.
7. Deploy the application using Google Cloud Platform.
8. Implement containerized services using Docker.
9. Establish CI/CD using GitHub Actions.
10. Implement an AI-assisted analytics workflow.
11. Demonstrate secure software development practices.
12. Maintain professional technical documentation throughout development.

## 4. Target Users

### Administrator

Responsible for:

- Managing users
- Managing roles
- Monitoring ETL executions
- Viewing system-level information

### Analyst

Responsible for:

- Exploring claims data
- Viewing cost analytics
- Viewing utilization analytics
- Running analytical queries
- Using the AI analytics assistant

### Viewer

Responsible for:

- Viewing dashboards
- Viewing reports
- Accessing read-only analytics

## 5. Core Features

### Data ingestion

The system will accept healthcare claims-like datasets containing information about:

- Members
- Providers
- Claims
- Claim lines
- Procedures
- Diagnoses

### ETL pipeline

The pipeline will:

1. Extract raw data.
2. Validate incoming records.
3. Clean invalid data.
4. Transform records into the application's data model.
5. Detect duplicates.
6. Perform data quality checks.
7. Load valid data into PostgreSQL.
8. Record pipeline execution results.

### Analytics

The application will provide:

- Total healthcare cost
- Cost per member
- Claim volume
- Provider cost analysis
- Cost trends
- Utilization trends
- High-cost members
- Year-over-year comparisons
- Provider rankings

### AI Analytics Assistant

Users will be able to ask natural-language questions about available analytics.

Example:

> Which providers had the highest increase in average claim cost?

The AI assistant will generate a read-only SQL query, validate the query, execute it against an appropriately restricted database user, and return an understandable response.

## 6. Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- PostgreSQL
- Pytest

### Frontend

- React
- TypeScript
- Vite
- React Router
- TanStack Query
- Zustand
- Recharts

### Data Engineering

- Python
- Pandas
- SQLAlchemy

### Cloud

- Google Cloud Run
- Google Cloud SQL
- Google Cloud Storage
- Google Cloud Functions
- Google Cloud Scheduler
- Google Cloud IAM
- Google Artifact Registry
- Firestore
- Firebase Authentication

### DevOps

- Docker
- Docker Compose
- GitHub Actions
- Terraform

## 7. Development Principles

The project will follow these principles:

- API-first development
- Separation of concerns
- Secure-by-default design
- Automated testing
- Containerized development
- Infrastructure as code
- Least-privilege access
- Reproducible deployments
- Meaningful Git commits
- Continuous documentation

## 8. Success Criteria

The project will be considered complete when:

- The backend provides documented REST APIs.
- The frontend consumes the backend APIs.
- The ETL pipeline processes realistic datasets.
- PostgreSQL contains normalized analytical data.
- Advanced SQL analytics are implemented.
- Authentication and authorization are implemented.
- Firestore is integrated.
- The AI assistant safely performs analytical queries.
- The application is deployed on GCP.
- CI/CD automatically tests and deploys the application.
- The system is documented sufficiently for another developer to run and understand it.
