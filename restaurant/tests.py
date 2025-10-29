from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Menu, Booking
from datetime import datetime, timedelta

class MenuModelTest(TestCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(
            title="Pizza Margherita",
            price=12.99,
            inventory=50
        )
        self.assertEqual(str(menu), "Pizza Margherita : 12.99")
        self.assertEqual(menu.title, "Pizza Margherita")
        self.assertEqual(menu.price, 12.99)
        self.assertEqual(menu.inventory, 50)

class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking_date = datetime.now() + timedelta(days=1)
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=booking_date
        )
        self.assertIn("John Doe", str(booking))
        self.assertIn("4 guests", str(booking))

class MenuAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.menu_data = {
            'title': 'Caesar Salad',
            'price': 8.99,
            'inventory': 30
        }

    def test_create_menu_item(self):
        response = self.client.post('/api/menu/', self.menu_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().title, 'Caesar Salad')

    def test_get_menu_items(self):
        Menu.objects.create(title='Pasta', price=15.99, inventory=25)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_menu_item(self):
        menu = Menu.objects.create(title='Burger', price=10.99, inventory=20)
        updated_data = {'title': 'Cheeseburger', 'price': 12.99, 'inventory': 20}
        response = self.client.put(f'/api/menu/{menu.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menu.refresh_from_db()
        self.assertEqual(menu.title, 'Cheeseburger')

    def test_delete_menu_item(self):
        menu = Menu.objects.create(title='Soup', price=6.99, inventory=15)
        response = self.client.delete(f'/api/menu/{menu.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)

class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.booking_data = {
            'name': 'Jane Smith',
            'no_of_guests': 2,
            'booking_date': '2024-12-25T19:00:00Z'
        }

    def test_create_booking(self):
        response = self.client.post('/api/bookings/', self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_get_bookings(self):
        Booking.objects.create(
            name='Test Booking',
            no_of_guests=4,
            booking_date=datetime.now() + timedelta(days=1)
        )
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

class AuthenticationTest(APITestCase):
    def test_user_registration(self):
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'newuser@example.com'
        }
        response = self.client.post('/api/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post('/api/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_unauthorized_access(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
