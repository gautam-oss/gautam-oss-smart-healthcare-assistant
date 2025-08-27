from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import DoctorSerializer
from .models import Doctor

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