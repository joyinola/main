from django.contrib import admin
from .models import bidding,comment,product,category,User
# Register your models here.
admin.site.register(bidding)
admin.site.register(comment)
admin.site.register(product)
admin.site.register(category)
admin.site.register(User)
