from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email


class FindBuddy(models.Model):
    GYM_CHOICES = (
        ("Wooden", 'John Wooden Center'),
        ("Bfit", 'Bruin Fitness Center'),
        ("LA", 'LA Fitness'),
    )
    gym = models.CharField(max_length=6,
                                      choices=GYM_CHOICES)


    arr=[]
    for i in range(6,13):
        for j in range(0,60,30):
            arr.append(str(i).zfill(2) + ":" + str(j).zfill(2) + " AM")
    TIME_CHOICES = []
    k = 0
    for val in arr:
        TIME_CHOICES.append((val ,val))
        k+=1

    arr = []
    for i in range(1,12):
        for j in range(0,60,30):
            arr.append(str(i).zfill(2) + ":" + str(j).zfill(2)+ " PM") 
    for val in arr:
        TIME_CHOICES.append((val ,val))
        k+=1

    time = models.CharField(max_length=8,
                                      choices=TIME_CHOICES)

    username = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
