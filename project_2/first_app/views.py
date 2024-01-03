from django.shortcuts import render


from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
   # return HttpResponse("This home page.")
    return render(request, "first_app/home.html")