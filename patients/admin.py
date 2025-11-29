from django.contrib import admin
from .models import Patient, HealthRecord

admin.site.register(Patient)
admin.site.register(HealthRecord)
