from django.contrib import admin
from assessment.models import Assessment


# Register your models here.
@admin.register(Assessment)
class RegistrationAdmin(admin.ModelAdmin):
    ...