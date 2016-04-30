from django import forms
from .models import SignUp
from .models import Student


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		### exclude = ['full_name'] use sparingly

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise form.ValidationError("Please make sure you use your USC email")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#write validation code
		return full_name

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['year_in_school']
		### exclude = ['full_name'] use sparingly

