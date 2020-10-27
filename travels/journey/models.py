from django.db import models

# Create your models here.
class City(models.Model):
	code=models.CharField(max_length=5)
	city=models.CharField(max_length=64)
	def __str__(self):
		return(f"{self.city} ({self.code})")

class Travel(models.Model):
	origin=models.ForeignKey(City, on_delete=models.CASCADE,related_name='departure')
	destination=models.ForeignKey(City,on_delete=models.CASCADE,related_name='arrivals')
	duration=models.IntegerField()
	def __str__(self):
		return(f"{self.id}. {self.origin} to {self.destination} time in minutes: {self.duration}")
class Passengers(models.Model):
	first=models.CharField(max_length=64)
	last= models.CharField(max_length=64)
	flight=models.ManyToManyField(Travel, blank=True,related_name='passengers')
	def __str__(self):
		return(f"{self.first} {self.last}")