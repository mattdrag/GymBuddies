from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import SignUpForm
from .forms import StudentForm
from .models import SignUp
from .models import Student
from celery.schedules import crontab
from datetime import timedelta

# Create your views here.
def home(request):
	title = 'Enter your info:'
	form = SignUpForm(request.POST or None)
	title2 = 'What year are you:'
	form2 = Student(request.POST or None)

	# if request.user.is_authenticated():
	# 	title = "My Title %s" %(request.user)
	
	context = {
		"title": title,
		"form": form,
		"title2": title2,
		"form2": form2,
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


	# if request.user.is_authenticated() and request.user.is_staff:
	# 	#print SignUp.objects.all()
	# 	# i = 1
	# 	# for instance in SignUp.objects.all():
	# 	# 	print i
	# 	# 	print instance.full_name
	# 	# 	i += 1
	# 	queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__icontains="Justin")
	# 	#print SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="Justin").count()
	# 	context = {
	# 		"queryset": queryset
	# 	}

	return render(request, "home.html", context)

