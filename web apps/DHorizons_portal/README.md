# DHorizons Portal

DHorizons Portal is a Flask-based web application developed for managing and presenting Digital Humanities content. The platform allows structured publication of posts, events, and lessons through an authenticated admin interface.

## Overview

The application includes a dynamic homepage displaying the most recent content, dedicated pages for posts, events, and lessons, an admin dashboard for content management, image upload functionality, event date handling, integrated search across content, and a custom Jinja filter for extracting YouTube video IDs.

The backend is implemented using Flask and SQLAlchemy, with SQLite as the database engine.

## Architecture

The project follows a standard Flask structure:

DHorizons_portal/
- app.py  
- create_db.py  
- templates/  
- static/  
- static/uploads/  
- instance/database.db  

Core technologies:

- Python  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- Jinja2  
- HTML / CSS  

## Data Models

The application defines three main database models:

- Post  
- Eventi  
- Lezioni  

Each model supports full CRUD operations through the admin panel.

## Key Functionalities

- Content creation and deletion (admin area)  
- Secure file upload handling  
- Date parsing and storage as Date objects  
- Search system using case-insensitive matching  
- Session-based authentication  
- Custom YouTube ID extraction filter  

## Running the Application

Install dependencies:

pip install flask flask_sqlalchemy

Run the application:

python app.py

Open in browser:

http://127.0.0.1:5000

## Admin Access

Login route:

/login

Default credentials (development only):

Username: admin  
Password: 1234  

## Purpose

This project demonstrates backend development with Flask, database modeling using SQLAlchemy, dynamic template rendering with Jinja, authentication through session handling, CRUD operations, and integration of a basic search system.

Developed within the context of Web Technologies and Digital Humanities coursework.
