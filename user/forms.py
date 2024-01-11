from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. Inform a valid email address.')
    phone_no = forms.CharField(max_length = 20, help_text='Required. Inform a valid phone number.')
    first_name = forms.CharField(max_length = 20, help_text='Required. Inform a valid first name.')
    last_name = forms.CharField(max_length = 20, help_text='Required. Inform a valid last name.')
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
