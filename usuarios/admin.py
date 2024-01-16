from django.contrib import admin
from usuarios.models import Registration


# Register your models here.
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    ...