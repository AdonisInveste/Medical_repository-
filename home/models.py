from django.db import models
from django.contrib.auth.models import User 
from Identity import settings 


# Create your models here.


class Identity_unique(models.Model):
	
	NIS = models.CharField(max_length = 200, primary_key = True)
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	
	Timestamp = models.DateTimeField(auto_now=True)
	