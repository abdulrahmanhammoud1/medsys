from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_appointment_email(patient_email, appointment_time):
    send_mail(
        "Appointment Confirmation",
        f"Your appointment is scheduled at {appointment_time}.",
        "no-reply@medsys.com",
        [patient_email],
        fail_silently=True,
    )