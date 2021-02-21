# from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# from todoproj.todoapp.templatetags import todoapp_filters
from todoapp.templatetags.todoapp_filters import all_set
from .models import ToDo

@receiver(post_save, sender=ToDo)
def create_user_profile(sender, instance,**kwargs):
    print(sender)
    print(instance)
    


@receiver(pre_save, sender=ToDo)
def update_todo_model(sender, instance,**kwargs):
    print("I am called")

