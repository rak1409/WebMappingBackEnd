from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return response.Response(res, status.HTTP_201_CREATED)

