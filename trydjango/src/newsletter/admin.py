from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp
from .forms import FindBuddyForm
from .models import FindBuddy

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp

class FindBuddyAdmin(admin.ModelAdmin):
	list_display = ["username", "email", "gym", "time"]
	form = FindBuddyForm
	# class Meta:
	# 	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(FindBuddy, FindBuddyAdmin)