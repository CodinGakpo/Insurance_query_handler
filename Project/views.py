from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Home App")
    return render(request,"Project/home.html")