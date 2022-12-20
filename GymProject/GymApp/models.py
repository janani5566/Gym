from django.db import models


# Create your models here.

class Register(models.Model):
	goal = (
			('weight loss', 'weight loss'),
			('weight gain', 'weight gain'),
			('Fat loss', 'Fat loss'),
			('endurance training', 'endurance training'),
			)
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	address = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	goal = models.TextField()
	gender = models.CharField(max_length=30)




	def __str__(self):
		return self.name


