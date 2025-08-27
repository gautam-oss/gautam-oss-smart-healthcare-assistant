from django.urls import path
from .views import PatientRegisterView, PatientLoginView, PatientProfileView

urlpatterns = [
    path('register/', PatientRegisterView.as_view(), name='patient_register'),
    path('login/', PatientLoginView.as_view(), name='patient_login'),
    path('profile/', PatientProfileView.as_view(), name='patient_profile'),
]