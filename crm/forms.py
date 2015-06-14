from django import forms

class UserForm(forms.Form):
	first_name = forms.CharField(label='First name', max_length=36)
	last_name = forms.CharField(label='Last name', max_length=36)
	organization = forms.CharField(label='Company Name', max_length=200)
	username = forms.CharField(label='Username', max_length=36)
	email = forms.EmailField(label='Email', max_length=200)
	password = forms.CharField(widget=forms.PasswordInput,label='Password', max_length=200)

class SigninForm(forms.Form):
	username = forms.CharField(label='Username', max_length=36)
	password = forms.CharField(widget=forms.PasswordInput,label='Password', max_length=200)

class IndividualForm(forms.Form):
	first_name = forms.CharField(label='First name', max_length=36)
	last_name = forms.CharField(label='Last name', max_length=36)
#	photo = forms.FileField()
	email = forms.EmailField(label='Email', max_length=200)
	title = forms.CharField(label='Title', max_length=36)
	address = forms.CharField(label='Address', max_length=200)
	bio = forms.CharField(label='BIO', max_length=2800, widget=forms.Textarea)
