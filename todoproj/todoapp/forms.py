from django.forms import ModelForm, fields
from .models import ToDo,Notes
from django import forms
class ToDoForm(ModelForm):
    
    class Meta:
        model = ToDo
        fields = ['title','description','due_date','important']
        # widgets = {
        #     'title': forms.TimeField(
		# 		attrs={
		# 			'class': 'form-control mb-2'
		# 			}
		# 		),
        #     'description': forms.Textarea(
		# 		attrs={
		# 			'class': 'form-control mb-2'
		# 			}
		# 		),
		# 	}


class NotesForm(ModelForm):
    
    class Meta:
        model = Notes
        fields = ['description','file']
        # widgets = {
        #     'title': forms.TextInput(
		# 		attrs={
		# 			'class': 'form-control'
		# 			}
		# 		),
        #     'content': forms.Textarea(
		# 		attrs={
		# 			'class': 'form-control'
		# 			}
		# 		),
		# 	}
