from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import base64
from rest_framework.authtoken.models import Token

def convertBase64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


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

@csrf_exempt
def login(request):
    print(request)
    try:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(user)
            # token = django.middleware.csrf.get_token(request)
            
            # token = convertBase64(username + ':' + password)
            token, created = Token.objects.get_or_create(user=user)

            resp = '{"token": "' + token.key +'", "msg":"Login successful"}';
            return HttpResponse(resp)
    except Exception as e:
        print('Error', e)
    
    return HttpResponse('{"msg":"Login failed"}')