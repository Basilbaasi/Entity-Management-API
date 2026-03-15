# Entity Management API

A Django REST Framework based API for managing hierarchical entities:

Vendor → Product → Course → Certification

The system provides CRUD operations for all entities, relational mappings between them, validation rules, and interactive API documentation using Swagger.

---

## Project Overview

This project implements a modular backend architecture using Django and Django REST Framework. It manages relationships between different business entities while enforcing validation rules to maintain data integrity.

Entities included:

- Vendor
- Product
- Course
- Certification

Mappings implemented:

- Vendor → Product
- Product → Course
- Course → Certification

Each mapping supports validation rules such as preventing duplicate relationships and enforcing a single primary mapping.

---

## Features

- CRUD APIs for all entities
- Relational mappings between entities
- Validation to prevent duplicate mappings
- Primary mapping constraint for relationships
- Modular Django app architecture
- Interactive API documentation using Swagger

---

## Tech Stack

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger documentation)
- SQLite (default database)

---

## Project Structure


Entity-Management-API
│
├── entity_management # Main project configuration
│
├── vendor # Vendor entity APIs
├── product # Product entity APIs
├── course # Course entity APIs
├── certification # Certification entity APIs
│
├── vendor_product_mapping
├── product_course_mapping
├── course_certification_mapping
│
├── manage.py
├── requirements.txt
├── README.md


---

## Setup Instructions

### 1. Clone the repository


git clone https://github.com/Basilbaasi/Entity-Management-API.git

cd Entity-Management-API


### 2. Create virtual environment


python -m venv env


### 3. Activate environment

Windows


env\Scripts\activate


Linux / Mac


source env/bin/activate


### 4. Install dependencies


pip install -r requirements.txt


### 5. Run database migrations


python manage.py migrate


### 6. Start the server


python manage.py runserver


Server will start at:


http://127.0.0.1:8000


---

## API Documentation

Swagger UI


http://127.0.0.1:8000/swagger/


ReDoc


http://127.0.0.1:8000/redoc/


These interfaces allow testing all APIs directly from the browser.

---

## API Endpoints

### Vendor APIs


GET /api/vendors/
POST /api/vendors/
GET /api/vendors/{id}/
PUT /api/vendors/{id}/
PATCH /api/vendors/{id}/
DELETE /api/vendors/{id}/


### Product APIs


GET /api/products/
POST /api/products/
GET /api/products/{id}/
PUT /api/products/{id}/
PATCH /api/products/{id}/
DELETE /api/products/{id}/


### Course APIs


GET /api/courses/
POST /api/courses/
GET /api/courses/{id}/
PUT /api/courses/{id}/
PATCH /api/courses/{id}/
DELETE /api/courses/{id}/


### Certification APIs


GET /api/certifications/
POST /api/certifications/
GET /api/certifications/{id}/
PUT /api/certifications/{id}/
PATCH /api/certifications/{id}/
DELETE /api/certifications/{id}/


---

## Mapping APIs

### Vendor → Product Mapping


GET /api/vendor-product-mappings/
POST /api/vendor-product-mappings/
GET /api/vendor-product-mappings/{id}/
PUT /api/vendor-product-mappings/{id}/
PATCH /api/vendor-product-mappings/{id}/
DELETE /api/vendor-product-mappings/{id}/


### Product → Course Mapping


GET /api/product-course-mappings/
POST /api/product-course-mappings/
GET /api/product-course-mappings/{id}/
PUT /api/product-course-mappings/{id}/
PATCH /api/product-course-mappings/{id}/
DELETE /api/product-course-mappings/{id}/


### Course → Certification Mapping


GET /api/course-certification-mappings/
POST /api/course-certification-mappings/
GET /api/course-certification-mappings/{id}/
PUT /api/course-certification-mappings/{id}/
PATCH /api/course-certification-mappings/{id}/
DELETE /api/course-certification-mappings/{id}/


---

## Validation Rules

- Duplicate mappings between entities are not allowed
- Each parent entity can have only one `primary_mapping=True`
- Foreign key relationships must reference valid entities

These rules ensure data consistency within the hierarchy.

---

## Author

Developed as part of a Django Backend Internship Assignment.
