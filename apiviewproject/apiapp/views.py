from django.shortcuts import render
from rest_framework.response import Response
from apiapp.models import empdetails
from apiapp.serializers import EmpdetailSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class EmpdetailsAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            emp = empdetails.objects.get(id=id)
            serializer = EmpdetailSerializer(emp)
            return Response(serializer.data)
        emp = empdetails.objects.all()
        serializer = EmpdetailSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpdetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        emp = empdetails.objects.get(pk=id)
        serializer = EmpdetailSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Record updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        emp = empdetails.objects.get(pk=id)
        emp.delete()
        return Response({'msg': 'Record Deleted'})
