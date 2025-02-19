from django.shortcuts import get_object_or_404, render
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class SignupView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class User(APIView):

    def get_object(self, pk): 
        return get_object_or_404(User, pk=pk) 
    
    def get(self, request, pk):
        accounts = self.get_object(pk) 
        serializer = UserSerializer(accounts) #
        return Response(serializer.data)
    

    def put(self, request, pk):
        accounts = self.get_object(pk) 
        serializer = UserSerializer(accounts, data=request.data, partial=True) 
        if serializer.is_valid(raise_exception=True):                      
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        accounts = self.get_object(pk)
        accounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



