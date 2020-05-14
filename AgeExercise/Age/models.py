from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=60)
	dob = models.DateField()
	deleted = models.BooleanField(default=False)