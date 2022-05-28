from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt



def check_register_for_errors(request):
    if not request.method == 'POST':
        return 'Request method must be POST'
    fields = ['email', 'password', 'group']
    for field in fields:
        if not field in request.POST:
            return 'Please provide a variable "{}" in your body.'.format(field)
    return None

@csrf_exempt
def register(request):
    error = check_register_for_errors(request)
    if error:
        return HttpResponse('{"msg":"' + error + '"}', status=400)
    else:
        user = User.objects.create_user(username=request.POST['email'],
                                 email=request.POST['email'],
                                 password=request.POST['password'])
        if user:
            profile = Profile.objects.create(group=request.POST['group'], user=user)
            print('Created profile:', profile)
            return HttpResponse('{"msg":"User has been created!"}', status=200)

        else:
        	return HttpResponse('{"msg":"Could not create user."}', status=500)

