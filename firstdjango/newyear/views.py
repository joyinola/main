from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def newyear(request):
	now=datetime.now()
	return render(request, 'newyear/index.html', {'date': now.month==1 and now.day==1 })