from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    # slug = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Gazal/Poem ' + self.title

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
