from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReportSerializer, AppointmentSerializer
from .models import Report, Appointment
from patients.models import Patient
from doctors.models import Doctor
import requests

class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class SubmitSymptomsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        symptoms = request.data.get('symptoms')
        if not symptoms:
            return Response({'error': 'Symptoms are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Call ML API for disease prediction
        try:
            ml_api_url = "http://ml-disease-api:8001/predict"
            response = requests.post(ml_api_url, json={'symptoms': symptoms})
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            prediction_result = response.json()
        except requests.exceptions.RequestException as e:
            return Response({'error': f'ML API error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save report
        report_data = {
            'patient': request.user.id,
            'report_type': 'symptom_prediction',
            'details': f'Symptoms: {symptoms}. Prediction: {prediction_result}'
        }
        serializer = ReportSerializer(data=report_data)
        if serializer.is_valid():
            serializer.save(patient=request.user)
            return Response(prediction_result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadXrayView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        xray_image = request.FILES.get('xray_image')
        if not xray_image:
            return Response({'error': 'X-ray image is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Call ML API for X-ray classification
        try:
            ml_api_url = "http://ml-xray-api:8002/classify"
            files = {'file': (xray_image.name, xray_image.read(), xray_image.content_type)}
            response = requests.post(ml_api_url, files=files)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            classification_result = response.json()
        except requests.exceptions.RequestException as e:
            return Response({'error': f'ML API error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save report
        report_data = {
            'patient': request.user.id,
            'report_type': 'xray_classification',
            'details': f'X-ray classification result: {classification_result}'
        }
        serializer = ReportSerializer(data=report_data)
        if serializer.is_valid():
            serializer.save(patient=request.user)
            return Response(classification_result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)