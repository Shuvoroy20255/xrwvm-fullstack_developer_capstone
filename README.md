# fullstack_developer_capstone

Full‑stack web application for a national car retailer.  
Built with Django (backend API + static pages) and React (frontend SPA).  
Deployed using Docker, Kubernetes and IBM Cloud Code Engine.

## Features
- User registration, login, logout
- View all dealerships, filter by state
- View dealer details and customer reviews
- Submit a review for a dealer
- Sentiment analysis of reviews (mock IBM Watson NLU)
- Admin panel for managing car makes/models and dealership data

## Technologies
- Backend: Django, Django REST Framework
- Frontend: React, Bootstrap
- Database: SQLite (development)
- Deployment: Docker, Kubernetes, IBM Cloud Code Engine
- CI/CD: GitHub Actions

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 16+
- Docker (optional)

### Backend Setup
```bash
cd server
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
