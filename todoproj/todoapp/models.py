from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    modified_at = models.DateTimeField(auto_now=timezone.now())
    completed_at = models.DateTimeField(auto_now_add=False,null=True)
    description = models.TextField()
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def complete_task(self):
        self.completed_at = timezone.now()
        return super().save()    

