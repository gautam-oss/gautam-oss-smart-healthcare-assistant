from django.urls import path
from .views import ReportListCreateView, ReportDetailView, AppointmentListCreateView, AppointmentDetailView, SubmitSymptomsView, UploadXrayView

urlpatterns = [
    path('reports/', ReportListCreateView.as_view(), name='report_list_create'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment_list_create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('submit-symptoms/', SubmitSymptomsView.as_view(), name='submit_symptoms'),
    path('upload-xray/', UploadXrayView.as_view(), name='upload_xray'),
]