from django.forms import ModelForm, fields
from .models import ToDo
class ToDoForm(ModelForm):
    
    class Meta:
        model = ToDo
        fields = ['title','description','due_date','important']
