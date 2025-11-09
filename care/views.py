from rest_framework import viewsets, permissions
from .models import Patient, Practitioner, Appointment
from .serializers import PatientSerializer, PractitionerSerializer, AppointmentSerializer
from .tasks import send_appointment_email

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("id")
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

class PractitionerViewSet(viewsets.ModelViewSet):
    queryset = Practitioner.objects.all().order_by("id")
    serializer_class = PractitionerSerializer
    permission_classes = [permissions.IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related("patient", "practitioner").all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        appointment = serializer.save()
        if appointment.patient.email:
            send_appointment_email.delay(
                appointment.patient.email,
                appointment.start_time.isoformat(),
            )