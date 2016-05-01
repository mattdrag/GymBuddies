from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import FindBuddyForm, SignUpForm
from .models import SignUp, FindBuddy
from django.contrib.auth.models import User

import smtplib

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you"
		}

	# if request.user.is_authenticated() and request.user.is_staff:
	if request.user.is_authenticated():
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1

		queryset = User.objects.all().order_by('-username') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
		context = {
			"queryset": queryset

		}

	return render(request, "home.html", context)



def find(request):
	# request.user.username  - get user name
	title = "Find a Buddy"
	title_align_center = True
	form = FindBuddyForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.username = request.user.username
		instance.email = request.user.email
                instance.save()
		# users = User.objects.all().order_by('-username')
		# find = FindBuddy.objects.all().order_by('-time').order_by('-gym')
		flag = 0
		matches = FindBuddy.objects.all().filter(gym__exact=instance.gym).filter(time__exact=instance.time)
		match = None

		for item in matches:
			if item.username!=request.user.username:
				flag=1
				match = item
				server = smtplib.SMTP( "smtp.gmail.com", 587 ) 
				server.starttls()
				server.login( "bloodsucker32123@gmail.com", "Xcode2015" )
				server.sendmail( "", item.email, "We found a match for you to go to " + str(item.gym) + " at " + str(item.time) + ". Your matches email is " + str(request.user.email))
				server.quit()
				item.delete()
                                instance.delete()
                                break


		context = {
			"title" : "Thank you",
			"username": instance.username + '!',
			# "users": users,
			"item": item,
			"flag": flag
		}
		return render(request, "forms.html", context)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}

	return render(request, "forms.html", context)
















