from rest_framework import viewsets, permissions
from .serializers import CourseSerializer
from django.shortcuts import render
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
