from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import PatientSerializer
from .models import Patient

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