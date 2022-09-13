from django.db import models

# Create your models here.


class TodoModel(models.Model):
    task = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
