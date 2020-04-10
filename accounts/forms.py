
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class feedbackform(forms.Form):
    name = forms.CharField(max_length=100,label='Your name:')
    email = forms.EmailField(label='Your email:')
    subject = forms.CharField(max_length=100, label ='Subject:')
    message = forms.CharField( widget=forms.Textarea, label='Message/Suggestions:')
