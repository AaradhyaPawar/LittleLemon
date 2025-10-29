# Little Lemon Restaurant API - Setup Guide

## Project Overview

This Django REST Framework API provides endpoints for managing menu items and table bookings for the Little Lemon restaurant.

## Features

- ✅ Django REST Framework API
- ✅ User registration and authentication with tokens (Djoser)
- ✅ Menu items CRUD operations
- ✅ Table booking CRUD operations
- ✅ MySQL database support (with SQLite fallback)
- ✅ Unit tests
- ✅ Static HTML content serving
- ✅ Admin interface

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Configuration

#### Option A: SQLite (Default - for testing)

The project is configured to use SQLite by default for easy testing.

#### Option B: MySQL (For production)

1. Install MySQL server
2. Create a database named 'LittleLemon'
3. Update the database configuration in `littlelemon/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run the Server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- `POST /api/registration/` - User registration (custom endpoint)
- `POST /api/login/` - User login (custom endpoint)
- `POST /api/auth/users/` - Djoser user registration
- `POST /api/auth/token/login/` - Djoser token login
- `POST /api/auth/token/logout/` - Djoser token logout

### Menu Items

- `GET /api/menu/` - List all menu items
- `POST /api/menu/` - Create new menu item
- `GET /api/menu/{id}/` - Get specific menu item
- `PUT /api/menu/{id}/` - Update menu item
- `DELETE /api/menu/{id}/` - Delete menu item

### Table Bookings

- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/{id}/` - Get specific booking
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Delete booking

## Testing with Insomnia/Postman

### 1. Register a User

```json
POST /api/registration/
{
    "username": "testuser",
    "password": "testpass123",
    "email": "test@example.com"
}
```

### 2. Login

```json
POST /api/login/
{
    "username": "testuser",
    "password": "testpass123"
}
```

### 3. Use Token for Authenticated Requests

Add header: `Authorization: Token your_token_here`

### 4. Create Menu Item

```json
POST /api/menu/
{
    "title": "Pizza Margherita",
    "price": 12.99,
    "inventory": 50
}
```

### 5. Create Booking

```json
POST /api/bookings/
{
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2024-12-25T19:00:00Z"
}
```

## Running Tests

```bash
python manage.py test
```

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/`

- Username: admin
- Password: admin123

## Static Content

Visit `http://localhost:8000/api/` to see the API documentation page.

## Git Repository

The project is initialized as a Git repository. To push to GitHub:

1. Create a new repository on GitHub
2. Add remote: `git remote add origin <your-repo-url>`
3. Push: `git push -u origin main`
