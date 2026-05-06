# Entity Management API

A modular Django REST Framework API for managing hierarchical business entities:

**Vendor → Product → Course → Certification**

The system supports full CRUD operations, relational mappings between entities, validation rules to protect data integrity, and interactive API documentation using Swagger.  
This project was built as a backend-focused API assignment and is designed to be tested through Postman and browser-based API docs.

---

## Overview

Entity Management API is built with Django and Django REST Framework to manage a structured hierarchy of related entities.  
Each entity can be created, read, updated, and deleted independently, while mapping APIs connect them in a controlled and validated way.

The application is designed to demonstrate:

- REST API design
- Modular backend architecture
- Relationship handling between entities
- Input validation and duplicate-prevention logic
- API documentation and testing workflow

---

## Entity Flow

```text
Vendor → Product → Course → Certification
Relationship Mappings
Vendor → Product
Product → Course
Course → Certification

Each mapping supports validation rules such as:

preventing duplicate relationships
enforcing only one primary mapping per parent entity
validating foreign key references before saving data

Features

CRUD APIs for all entities
Relational mapping APIs between hierarchical entities
Validation to prevent duplicate and invalid mappings
Primary mapping constraint support
Modular Django app structure
Swagger-based interactive API documentation
Postman-friendly request workflow

Tech Stack

Python
Django
Django REST Framework
drf-yasg (Swagger documentation)
SQLite (default database)

Project Structure

Entity-Management-API/
│
├── entity_management/            # Main project configuration
├── vendor/                       # Vendor entity APIs
├── product/                      # Product entity APIs
├── course/                       # Course entity APIs
├── certification/                # Certification entity APIs
├── vendor_product_mapping/       # Vendor → Product mapping APIs
├── product_course_mapping/       # Product → Course mapping APIs
├── course_certification_mapping/ # Course → Certification mapping APIs
├── manage.py
├── requirements.txt
└── README.md

Setup Instructions

1. Clone the repository

git clone https://github.com/Basilbaasi/Entity-Management-API.git
cd Entity-Management-API

2. Create a virtual environment

python -m venv env

3. Activate the environment

Windows

env\Scripts\activate

Linux / Mac

source env/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Run migrations

python manage.py migrate

6. Start the development server

python manage.py runserver

The server will run at:

http://127.0.0.1:8000


API Documentation

Swagger UI

http://127.0.0.1:8000/swagger/

ReDoc

http://127.0.0.1:8000/redoc/

Both interfaces can be used to test and inspect the APIs directly from the browser.

API Endpoints

Vendor APIs

GET    /api/vendors/
POST   /api/vendors/
GET    /api/vendors/{id}/
PUT    /api/vendors/{id}/
PATCH  /api/vendors/{id}/
DELETE /api/vendors/{id}/

Product APIs

GET    /api/products/
POST   /api/products/
GET    /api/products/{id}/
PUT    /api/products/{id}/
PATCH  /api/products/{id}/
DELETE /api/products/{id}/

Course APIs

GET    /api/courses/
POST   /api/courses/
GET    /api/courses/{id}/
PUT    /api/courses/{id}/
PATCH  /api/courses/{id}/
DELETE /api/courses/{id}/

Certification APIs

GET    /api/certifications/
POST   /api/certifications/
GET    /api/certifications/{id}/
PUT    /api/certifications/{id}/
PATCH  /api/certifications/{id}/
DELETE /api/certifications/{id}/

Mapping APIs

Vendor → Product Mapping

GET    /api/vendor-product-mappings/
POST   /api/vendor-product-mappings/
GET    /api/vendor-product-mappings/{id}/
PUT    /api/vendor-product-mappings/{id}/
PATCH  /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/

Product → Course Mapping

GET    /api/product-course-mappings/
POST   /api/product-course-mappings/
GET    /api/product-course-mappings/{id}/
PUT    /api/product-course-mappings/{id}/
PATCH  /api/product-course-mappings/{id}/
DELETE /api/product-course-mappings/{id}/

Course → Certification Mapping

GET    /api/course-certification-mappings/
POST   /api/course-certification-mappings/
GET    /api/course-certification-mappings/{id}/
PUT    /api/course-certification-mappings/{id}/
PATCH  /api/course-certification-mappings/{id}/
DELETE /api/course-certification-mappings/{id}/

Validation Rules

Duplicate mappings between entities are not allowed
Each parent entity can have only one primary_mapping=True
Foreign key relationships must reference valid entities

These constraints ensure consistent and reliable hierarchical data handling.

Example API Workflow

Create a Vendor
Create a Product linked to that Vendor
Create a Course linked to the Product
Create a Certification linked to the Course
Validate the hierarchy through mapping APIs and Swagger/Postman

This workflow demonstrates the full nested entity relationship supported by the system.

Notes

This project is optimized for backend API testing
Postman can be used to create, update, and validate entities
No frontend is required for core functionality
The repo is designed to demonstrate clean backend structure and REST API design

Author

Developed by Basil C K
As part of a Django Backend Internship Assignment