from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EmployeeModel
from .serializer import EmployeeSerializer


class Employee(APIView):

    def get(self, request):
        objects = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(objects, many=True)
        return Response(serializer.data)



class GetLevel(APIView):

    def get(request, level):
        objects = EmployeeModel.objects.filter(level=level)
        serializer = EmployeeSerializer(objects)
        return Response(serializer.data)
