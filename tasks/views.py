from django.http import HttpResponse
from django.shortcuts import render
import django
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import JsonResponse
from django.core import serializers
import datetime

@csrf_exempt
def login(request):
    print(request)
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = django.middleware.csrf.get_token(request)
            resp = '{"token": "' + token +'", "msg":"Login successful"}';
            return HttpResponse(resp)
    except Exception:
        pass
    
    return HttpResponse('{"msg":"Login failed"}')

def check_task_for_errors(request):
    fields = ['group', 'title', 'description', 'category', 'urgency', 'due_date']
    for field in fields:
        if not field in request.POST:
            return 'Please provide a variable "{}" in your body.'.format(field)
    return None

# https://stackoverflow.com/questions/15874233/output-django-queryset-as-json
def task(request):
    if request.method =='POST':
        error_message = check_task_for_errors(request)
        if error_message:
            return HttpResponse('{"msg":"' + error_message + '"}')
        else:
            due_date = datetime.datetime.strptime(request.POST['due_date'], "%Y-%m-%d")


            task = Task.objects.create(
                group=request.POST['group'],
                title=request.POST['title'],
                description=request.POST['description'],
                category=request.POST['category'],
                urgency=request.POST['urgency'],
                due_date=due_date,
            )
            serialized_obj = serializers.serialize('json', [ task, ])
            return HttpResponse(serialized_obj[1:-1], content_type='application/json')
    else:
        data = list(Task.objects.values()) 
        return JsonResponse(data, safe=False) 

    return HttpResponse('{"msg":"not implemented yet"}')

def task_detail(request, id):
    data = Task.objects.get(id=id) 
    serialized_obj = serializers.serialize('json', [ data, ])
    return HttpResponse(serialized_obj[1:-1], content_type='application/json')
