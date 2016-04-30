from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import SignUpForm
from .forms import FindBuddyForm
from .models import SignUp
from .models import FindBuddy
from celery.schedules import crontab
from datetime import timedelta

# Create your views here.
def home(request):
	return render(request, "home.html")


def create(request):
	title = 'Enter your info:'
	form = SignUpForm(request.POST or None)

	# if request.user.is_authenticated():
	# 	title = "My Title %s" %(request.user)
	
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "test"
		instance.full_name = full_name
		instance.save()
		context = {
			"title" : "Thank you",
			"full_name": full_name,
		}


	return render(request, "create.html", context)

def find(request):
	title = 'Find a Buddy:'
	form = FindBuddyForm(request.POST or None)

	# if request.user.is_authenticated():
	# 	title = "My Title %s" %(request.user)
	
	context = {
		"title": title,
		"form": form,
	}

	if form.is_valid():
		form.save()
		# instance = form.save(commit=False)
		# full_name = form.cleaned_data.get("full_name")
		# if not full_name:
		# 	full_name = "test"
		# instance.full_name = full_name
		# instance.save()
		# context = {
		# 	"title" : "Thank you",
		# 	"full_name": full_name,
		# }


	return render(request, "find.html", context)

