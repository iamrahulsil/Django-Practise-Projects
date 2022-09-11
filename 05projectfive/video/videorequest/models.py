from django.db import models
from django.utils import timezone

# Create your models here.


class VideoReq(models.Model):
    videotitle = models.CharField(max_length=20)
    videodesc = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Name: {}, ID: {}".format(self.videotitle, self.pk)
