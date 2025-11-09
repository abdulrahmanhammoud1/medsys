from rest_framework import serializers
from .models import Patient, Practitioner, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class PractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practitioner
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    practitioner = PractitionerSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source="patient", write_only=True)
    practitioner_id = serializers.PrimaryKeyRelatedField(queryset=Practitioner.objects.all(), source="practitioner", write_only=True)

    class Meta:
        model = Appointment
        fields = ["id","patient","practitioner","patient_id","practitioner_id","start_time","end_time","reason","status","created_at"]
        read_only_fields = ["id","created_at"]