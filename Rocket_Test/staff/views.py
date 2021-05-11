from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmployeeModel
from .serializer import EmployeeSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class Employee(APIView):
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]
    def get(self, request):
        objects = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(objects, many=True)
        return Response(serializer.data)



class GetLevel(APIView):
    permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]
    def get(self, request, level):
        objects = EmployeeModel.objects.filter(level=level)
        serializer = EmployeeSerializer(objects, many=True)
        return Response(serializer.data)
