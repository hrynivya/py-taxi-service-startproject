from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ['username', 'license_number', 'first_name', 'last_name']
    search_fields = ['username', 'license_number']

    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'manufacturer']
    search_fields = ['model']
    list_filter = ['manufacturer']
    filter_horizontal = ['drivers']