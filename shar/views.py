from django.shortcuts import render, HttpResponse
from .tasks import create_user


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World!</h1>')


def make_user(request):
    create_user.delay(request.GET['username'], request.GET['email'], request.GET['password'])
    return HttpResponse('<h1>New user will be made</h1>')


def make_user_in_10_min(request):
    create_user.apply_async(args=[request.GET['username'], request.GET['email'], request.GET['password']], countdown=600)
    return HttpResponse('<h1>New user will be made in 10 minutes</h1>')