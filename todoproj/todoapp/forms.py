from django.forms import ModelForm, fields, widgets,Textarea
from .models import ToDo,Notes
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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


# class NotesForm(ModelForm):
    
#     class Meta:
#     	model = Notes
#     	fields = ['description','file']



class NotesForm(ModelForm):
	description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
	class Meta:
		model = Notes
		fields = ['description','file']
	def __init__(self,*args, **kwargs ) -> None:
		super().__init__(*args, **kwargs)
		self.fields['description'].widget.attrs.update({'class': 'mb-0'})
		
		