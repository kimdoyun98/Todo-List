from .models import Main_Todo
from django import forms


class Add_form(forms.ModelForm):
    class Meta:
        model = Main_Todo
        fields = ('context', 'end_date')