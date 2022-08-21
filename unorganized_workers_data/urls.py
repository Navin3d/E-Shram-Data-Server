from django.urls import path
from .views import EmployeeView, schema_view

urlpatterns = [
    path("employee/", EmployeeView.as_view(), name="employees"),
    path("swagger-ui/", schema_view)
]