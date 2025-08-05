from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Studentform(forms.ModelForm):  # Capitalized class name
    class Meta:
        model = Student
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']



