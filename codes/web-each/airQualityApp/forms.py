from django import forms
from .models import EmailList

class EmailListForm(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = '__all__'
    