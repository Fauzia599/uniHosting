from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
from urllib.parse import unquote
import json
from django.views.decorators.csrf import csrf_exempt


@permission_classes(IsAuthenticated)
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'DELETE', 'PUT'])
    

    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance =model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            if id:
                try:
                    instance =model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
                
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'})
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
    return api

manage_Cleaner= generic_api(Cleaner, CleanerSerializar)
manage_Task= generic_api(Task,TaskSerializar)





# CLEANER LOGIN
class AdminLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            # Attempt to retrieve the clener by email
            admin = Admin.objects.get(email=email,password=password)

            if admin is not None:
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid Email Or Password"}, status=status.HTTP_401_UNAUTHORIZED)
        except Admin.DoesNotExist:
            return Response({"message": "Invalid Email Or Password"}, status=status.HTTP_401_UNAUTHORIZED)


# CLEANER LOGIN
class CleanerLoginView(APIView):
    def post(self, request):
        Email = request.data.get('Email')
        Password = request.data.get('Password')

        try:
            # Attempt to retrieve the clener by email
            cleaner = Cleaner.objects.get(Email=Email,Password=Password)

            if cleaner is not None:
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid Email Or Password"}, status=status.HTTP_401_UNAUTHORIZED)
        except Cleaner.DoesNotExist:
            return Response({"message": "Invalid Email Or Password"}, status=status.HTTP_401_UNAUTHORIZED)


