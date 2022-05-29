from django.http import HttpResponse
from django.shortcuts import render
import django
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from userinfo.models import Profile
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
        # kwargs = self.kwargs
        # print(kwargs)
        profile = Profile.objects.get(user=self.request.user)
        return Task.objects.filter(group=profile.group)

    def create(self, request, *args, **kwargs):
        print('POST CALLED')
        profile = Profile.objects.get(user=self.request.user)
        due_date = datetime.datetime.strptime(request.POST['due_date'], "%Y-%m-%d")
        task = Task.objects.create(
                group=profile.group,
                title=request.POST['title'],
                description=request.POST['description'],
                category=request.POST['category'],
                urgency=request.POST['urgency'],
                due_date=due_date,
            )
        serialized_obj = serializers.serialize('json', [ task, ])
        return HttpResponse(serialized_obj[1:-1], content_type='application/json')
