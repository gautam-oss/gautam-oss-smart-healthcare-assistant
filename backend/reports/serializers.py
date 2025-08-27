from rest_framework import serializers
from .models import Report, Appointment

class ReportSerializer(serializers.ModelSerializer):
    patient_username = serializers.ReadOnlyField(source='patient.username')
    doctor_username = serializers.ReadOnlyField(source='doctor.username')

    class Meta:
        model = Report
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient_username = serializers.ReadOnlyField(source='patient.username')
    doctor_username = serializers.ReadOnlyField(source='doctor.username')

    class Meta:
        model = Appointment
        fields = '__all__'