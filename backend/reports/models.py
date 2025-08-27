from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    report_type = models.CharField(max_length=100) # e.g., 'symptom_prediction', 'xray_classification'
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.patient.username} ({self.report_type})"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=50, default='scheduled') # e.g., scheduled, completed, cancelled
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient.username} with Dr. {self.doctor.username} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"