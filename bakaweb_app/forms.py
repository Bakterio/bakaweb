from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('url', 'user_name', 'pw')