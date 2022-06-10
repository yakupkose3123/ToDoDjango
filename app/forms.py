from django import forms
from .models import TODO


class ToDoForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = "__all__"