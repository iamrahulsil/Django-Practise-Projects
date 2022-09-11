from django.shortcuts import render

# Create your views here.
from .models import VideoReq


def index(request):
    videoModel = VideoReq.objects.order_by("-date_added")
    context = {'videos': videoModel}
    return render(request, "videorequest/index.html", context)


def vrform(request):
    return render(request, "videorequest/vrform.html")
