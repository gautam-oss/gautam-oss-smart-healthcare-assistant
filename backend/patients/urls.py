from django.urls import path
from .views import PatientRegisterView, PatientLoginView, PatientProfileView, SubmitSymptomsView

urlpatterns = [
    path('register/', PatientRegisterView.as_view(), name='patient_register'),
    path('login/', PatientLoginView.as_view(), name='patient_login'),
    path('profile/', PatientProfileView.as_view(), name='patient_profile'),
    path('submit-symptoms/', SubmitSymptomsView.as_view(), name='submit_symptoms'),
]