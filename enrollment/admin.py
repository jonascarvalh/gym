from django.contrib import admin
from enrollment.models import Registration


# Register your models here.
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    ...