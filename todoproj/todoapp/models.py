from typing import Optional,Iterable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
from django.utils import timezone
# Create your models here.

class DateTimeFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    modified_at = models.DateTimeField(auto_now = timezone.now())



class ToDo(models.Model):
    title = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    modified_at = models.DateTimeField(auto_now=timezone.now())
    completed_at = models.DateTimeField(auto_now_add=False,null=True)
    due_date  = models.DateTimeField(auto_now_add=False,null=False,blank=False,default=timezone.now())
    description = models.TextField()
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def complete_task(self):
        self.completed_at = timezone.now()
        return super().save()    

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    todo = models.ForeignKey(ToDo,on_delete=models.CASCADE)
    description = models.TextField(help_text="Add your Note Here")  
    created_at = models.DateTimeField(auto_now_add=timezone.now())
    modified_at = models.DateTimeField(auto_now=timezone.now())
    file = models.ImageField(upload_to = 'images/',null = True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    

    def __str__(self) -> str:
        return str(self.todo) + str(self.user)
    

   


    

