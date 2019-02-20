from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title