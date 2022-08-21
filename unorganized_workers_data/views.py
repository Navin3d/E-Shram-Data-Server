from webbrowser import get

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view

from .models import Employees
from .serializers import EmployeesSerializers


schema_view = get_swagger_view(title="aois")


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
