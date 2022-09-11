from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "videorequest/index.html")


def vrform(request):
    return render(request, "videorequest/vrform.html")
