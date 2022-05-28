from django.http import HttpResponse
from django.shortcuts import render
import django
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import JsonResponse
from django.core import serializers
import datetime
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        kwargs = self.kwargs
        # print(kwargs)
        return Task.objects.filter(group=123)
