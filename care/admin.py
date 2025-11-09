from django.contrib import admin
from .models import Patient, Practitioner, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","birth_date","gender","phone","email","created_at")
    search_fields = ("first_name","last_name","email","phone")

@admin.register(Practitioner)
class PractitionerAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","specialty","license_id")
    search_fields = ("first_name","last_name","specialty","license_id")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id","patient","practitioner","start_time","end_time","status")
    list_filter = ("status",)