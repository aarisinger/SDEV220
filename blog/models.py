from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    created_at=models.DateField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return self.title