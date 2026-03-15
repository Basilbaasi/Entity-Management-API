# Entity Management API

A Django REST API for managing hierarchical entities:

Vendor → Product → Course → Certification

---

## Tech Stack

- Django
- Django REST Framework
- drf-yasg (Swagger API documentation)
- SQLite (default)

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Basilbaasi/Entity-Management-API.git
cd Entity-Management-API

2. Create virtual environment
python -m venv env
3. Activate environment

Windows

env\Scripts\activate

Linux/Mac

source env/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Run migrations
python manage.py migrate

6. Start server
python manage.py runserver

Server runs at:

http://127.0.0.1:8000
API Documentation

Swagger UI:

http://127.0.0.1:8000/swagger/

ReDoc:

http://127.0.0.1:8000/redoc/
API Structure
Master APIs

/api/vendors/

/api/products/

/api/courses/

/api/certifications/

Mapping APIs

/api/vendor-product-mappings/

/api/product-course-mappings/

/api/course-certification-mappings/

Features

CRUD APIs for all entities

Mapping relationships

Duplicate mapping prevention

Single primary mapping validation

Swagger interactive documentation

Author

Developed as part of a Django Backend Assignment.
