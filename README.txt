Little Lemon Restaurant API

API Endpoints for Testing:

Authentication:
POST /api/registration/ - User registration
POST /api/login/ - User login

Menu Items:
GET /api/menu/ - List all menu items
POST /api/menu/ - Create new menu item
GET /api/menu/{id}/ - Get specific menu item
PUT /api/menu/{id}/ - Update menu item
DELETE /api/menu/{id}/ - Delete menu item

Table Bookings:
GET /api/bookings/ - List all bookings
POST /api/bookings/ - Create new booking
GET /api/bookings/{id}/ - Get specific booking
PUT /api/bookings/{id}/ - Update booking
DELETE /api/bookings/{id}/ - Delete booking

Authentication Required:
All endpoints except registration and login require authentication.
Include the token in the Authorization header: "Authorization: Token your_token_here"

Sample Data for Testing:

Registration:
{
    "username": "testuser",
    "password": "testpass123",
    "email": "test@example.com"
}

Login:
{
    "username": "testuser",
    "password": "testpass123"
}

Menu Item:
{
    "title": "Pizza Margherita",
    "price": 12.99,
    "inventory": 50
}

Booking:
{
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2024-12-25T19:00:00Z"
}
