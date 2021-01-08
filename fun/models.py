from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Upload(models.Model):
    your_name = models.CharField(max_length=20)
    opponent_name = models.CharField(max_length=20)
    your_video = models.FileField()
    opponent_video = models.FileField()
    date_posted = models.DateTimeField(default=timezone.now)
    your_video_likes = models.IntegerField(default=0)
    opponent_video_likes = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.your_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
