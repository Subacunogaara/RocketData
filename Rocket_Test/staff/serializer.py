from rest_framework import serializers
from .models import EmployeeModel



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields ='__all__'
        depth = 5
