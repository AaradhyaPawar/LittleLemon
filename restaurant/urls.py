from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('', include(router.urls)),
]
