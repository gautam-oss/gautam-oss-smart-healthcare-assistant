from django.urls import path
from .views import DoctorRegisterView, DoctorLoginView, DoctorProfileView, UploadXRayView

urlpatterns = [
    path('register/', DoctorRegisterView.as_view(), name='doctor_register'),
    path('login/', DoctorLoginView.as_view(), name='doctor_login'),
    path('profile/', DoctorProfileView.as_view(), name='doctor_profile'),
    path('upload-xray/', UploadXRayView.as_view(), name='upload_xray'),
]