from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Student
import time
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

# Create your views here.


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_context(self):
        return {"request":self.request}