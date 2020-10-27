from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
	watchlist=models.ManyToManyField('product',blank=True,related_name='person')
	def __str__(self):
		return(self.username)
class category(models.Model):
	choices=(
		('Fashion','Fashion'),
		('Gadgets','Gadgets'),
		('Clothes','Clothes'),
		('Shoes','Shoes'),
		('Food','Food'),
		('Medications','Medications'),
		('Art', 'Art'),
		('Skincare','Skincare'),
		('Makeup','Makeup')


		)
	category=models.CharField(max_length=255, choices=choices,default='Fashion', blank=True)
	def __str__(self):
		return(f"{self.category}")
class comment(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	comment=models.TextField(max_length=255, blank=True)
	def __str__(self):
		return(f"{self.comment} by:{self.user}")
class product(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='product')
	item=models.CharField(max_length=255,blank=True)
	img=models.URLField(max_length=255,blank=True, null=True)
	description=models.TextField(max_length=255,blank=True)
	price=models.DecimalField(max_digits=255, decimal_places=2)
	category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True)
	comment=models.ManyToManyField(comment,blank=True)
	is_active=models.BooleanField(default=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	
	def __str__(self):
		return(f"Item: {self.item}, Price:{self.price}, img:{self.img},comment:{self.comment} description:{self.description},category:{self.category}, user:{self.user}")

class bidding(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	item_price=models.DecimalField(max_digits=255,decimal_places=2,default=0)
	listing=models.ForeignKey(product, on_delete=models.CASCADE,blank=True)
	def __str__(self):
		return(f"{self.item_price} by:{self.user}")

