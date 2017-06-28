from django import forms
from guardian.models import Credentials



class CredentialsForm(forms.ModelForm):

	class Meta:
		model = Credentials
		fields = ["name", "url", "password"]
		widgets = {
			'name':forms.TextInput(attrs = {'placeholder': 'Name', 'class': 'form-control'}),
			'url':forms.TextInput(attrs = {'placeholder': 'Url', 'class': 'form-control'}),
			'password':forms.TextInput(attrs = {'placeholder': 'Password', 'class': 'form-control'}),
		}