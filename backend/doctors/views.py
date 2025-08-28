from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import DoctorSerializer
from .models import Doctor
from reports.models import Report
import requests
import base64
import io

class DoctorRegisterView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (permissions.AllowAny,)

class DoctorLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        doctor = Doctor.objects.filter(username=username).first()

        if doctor and doctor.check_password(password):
            refresh = RefreshToken.for_user(doctor)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': DoctorSerializer(doctor).data,
            })
        return Response({'detail': 'Invalid credentials'}, status=400)

class DoctorProfileView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class UploadXRayView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if 'xray_image' not in request.FILES:
            return Response({'error': 'No X-ray image provided'}, status=status.HTTP_400_BAD_REQUEST)

        xray_image = request.FILES['xray_image']

        # Read image as bytes and encode to base64
        image_bytes = xray_image.read()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')

        try:
            # Call ML X-ray classification API
            ml_api_url = "http://ml-xray-api:5000/predict"
            response = requests.post(ml_api_url, json={'image': encoded_image})
            response.raise_for_status()  # Raise an exception for HTTP errors
            classification_result = response.json()

            # Save report
            Report.objects.create(
                doctor=request.user,
                report_type='xray_classification',
                details=f"X-ray classification: {classification_result.get('prediction')}"
            )

            return Response(classification_result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Error connecting to ML service: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': f'An unexpected error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)