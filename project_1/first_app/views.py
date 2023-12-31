from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("This is Home page.")
def courses(request):
    return HttpResponse("This is First_app/course page.")