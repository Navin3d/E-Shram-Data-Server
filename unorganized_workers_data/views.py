from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Employees
from .serializers import EmployeesSerializers


class EmployeeView(APIView):
    def get(self, request):
        found_employees = Employees.objects.all()
        serialized_employees = EmployeesSerializers(found_employees, many=True)
        return Response(serialized_employees.data, status=status.HTTP_200_OK)

    def post(self, request):
        datas = request.data
        print(datas)
        for data in datas:
            Employees.objects.create(**data)
        return Response("Employees Added Successfully...", status=status.HTTP_200_OK)

    def delete(self, request):
        Employees.objects.all().delete()
        return Response("Employees deleted Successfully...", status=status.HTTP_200_OK)
