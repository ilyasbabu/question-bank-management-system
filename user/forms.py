from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
	name = forms.CharField(label = ("Full Name"))
	username = forms.EmailField(label = ("Email"))
	password1 = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-red-200 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full'}))
	password2 = forms.CharField(label=('Password confirm'),widget=forms.PasswordInput(attrs={'class':'py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-red-200 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full'}))

	class Meta:
		model = User
		fields = ('name', 'username', 'password1', 'password2')
		widgets={
			'password1': forms.PasswordInput(attrs={
				'class': 'py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-red-200 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full'
			}),
		}

