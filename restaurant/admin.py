from django.contrib import admin
from .models import Menu, Booking

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory']
    list_filter = ['price']
    search_fields = ['title']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'no_of_guests', 'booking_date']
    list_filter = ['booking_date', 'no_of_guests']
    search_fields = ['name']
