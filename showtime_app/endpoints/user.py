from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from showtime_app.models import CustomUser
from showtime_app.serializers import UserSerializer, CustomRegisterSerializer
from dj_rest_auth.registration.views import RegisterView


class ListAllUsers(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


class DeleteUser(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny, ]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     # serializer.is_valid(raise_exception=True)
    #     # self.perform_create(serializer)
    #     # headers = self.get_success_headers(serializer.data)
    #     # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response({'detail': 'Verification e-mail sent.'}, status=status.HTTP_201_CREATED)
    #
