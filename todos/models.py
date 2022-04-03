from statistics import mode
from turtle import title
from helpers.models import TrackingModel
from django.db import models
from authentication.models import User

# Create your models here.

class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    Owner = models.ForeignKey(to=User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
