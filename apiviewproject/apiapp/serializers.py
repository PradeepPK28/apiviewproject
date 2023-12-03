from rest_framework import serializers
from apiapp.models import empdetails


class EmpdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = empdetails
        fields = ['id', 'name', 'dept_name', 'city', 'phone_no']
