from django.shortcuts import get_object_or_404, render
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class SignupView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class UserDetailView(APIView):

    permission_classes = [IsAuthenticated] # 유저가 아니면 Article 기능 접근 제한

    def get_object(self, username):  # pk -> username
        return get_object_or_404(User, username=username)  # pk=pk -> username=username
    
    def get(self, request, username):  # pk -> username
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):  # pk -> username
        user = self.get_object(username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, username):  # pk -> username
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    