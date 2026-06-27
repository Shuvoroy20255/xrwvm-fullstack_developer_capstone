# Cars Dealership - Full Stack Capstone Project

## Project Name

Cars Dealership - National Car Retailer Web Application

## Description

A responsive full-stack web application that displays U.S. dealership branches, allows users to view dealers, filter by state, and submit reviews with IBM Watson sentiment analysis.
Built with React, Django, Node.js microservices, MongoDB, and SQLite. Deployed using Docker, Kubernetes, and IBM Cloud Code Engine.

## Technologies

- **Frontend**: React, HTML5, CSS3, Bootstrap
- **Backend**: Django, Django REST Framework, Node.js, Express
- **Databases**: SQLite, MongoDB
- **Cloud**: IBM Cloud Code Engine, IBM Watson NLU
- **DevOps**: Docker, Kubernetes, GitHub Actions

## Features

- User authentication (register, login, logout)
- Browse all dealerships
- Filter dealerships by state
- View dealer details & reviews
- Submit reviews with automatic sentiment analysis
- Admin panel for managing data
- Fully responsive design

## Installation & Local Run

```bash
git clone https://github.com/your-github-username/cars-dealership.git
cd cars-dealership/server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
