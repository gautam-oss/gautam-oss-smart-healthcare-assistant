from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import PatientSerializer
from .models import Patient
from reports.models import Report
import requests

class PatientRegisterView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.AllowAny,)

class PatientLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        patient = Patient.objects.filter(username=username).first()

        if patient and patient.check_password(password):
            refresh = RefreshToken.for_user(patient)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': PatientSerializer(patient).data,
            })
        return Response({'detail': 'Invalid credentials'}, status=400)

class PatientProfileView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class SubmitSymptomsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        symptoms = request.data.get('symptoms')
        if not symptoms:
            return Response({'error': 'Symptoms are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call ML disease prediction API
            ml_api_url = "http://ml-disease-api:5000/predict"
            response = requests.post(ml_api_url, json={'symptoms': symptoms})
            response.raise_for_status()  # Raise an exception for HTTP errors
            prediction_result = response.json()

            # Save report
            Report.objects.create(
                patient=request.user,
                report_type='symptom_prediction',
                details=f"Symptoms: {symptoms}, Prediction: {prediction_result.get('prediction')}"
            )

            return Response(prediction_result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Error connecting to ML service: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': f'An unexpected error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)