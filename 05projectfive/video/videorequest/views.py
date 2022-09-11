from django.shortcuts import render

# Create your views here.
from .models import VideoReq


def index(request):
    videoModel = VideoReq
    context = {'videos': videoModel}
    return render(request, "videorequest/index.html", context)


def vrform(request):
    return render(request, "videorequest/vrform.html")
