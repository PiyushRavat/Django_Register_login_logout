from django import forms
from .models import*
from django.contrib.auth.models import User

class userformA(forms.ModelForm):
	username = forms.CharField(label="Username", required=True, max_length=30)
	email    = forms.CharField(label="Email", required=True, max_length=30)
	first_name = forms.CharField(label="first_name", required=True, max_length=20)
	password = forms.CharField(label="ppassword", required=True, max_length=10)

	class Meta():
		model = User
		fields = ['username', 'email', 'first_name', 'password']

