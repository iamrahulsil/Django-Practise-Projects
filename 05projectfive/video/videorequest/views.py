from django.shortcuts import render, redirect

# Create your views here.
from .models import VideoReq
from .forms import VideoForm


def index(request):
    videoModel = VideoReq.objects.order_by("-date_added")
    context = {'videos': videoModel}
    return render(request, "videorequest/index.html", context)


def vrform(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            new_req = VideoReq(
                videotitle=request.POST['videoname'],
                videodesc=request.POST['videodesc'],
            )
            new_req.save()

            return redirect('index')
    else:
        form = VideoForm()

    context = {'forms': form}

    return render(request, "videorequest/vrform.html", context)
