from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class tasks(forms.Form):
	task=forms.CharField(label='New Task')
	
def home(request):
	if 'tasks' not in request.session:
		request.session['tasks']=[]
	items=request.session['tasks']
	return render(request, 'tasks/index.html',{'items': items})
	

def task(request):
	if request.method=="POST":
		data=tasks(request.POST)
		if data.is_valid():
			cleaned=data.cleaned_data['task']
			
			request.session['tasks']+=[cleaned]
			return HttpResponseRedirect(reverse("home"))
		else:
			return render(request,'tasks/addtask.html',{'task':data})
	return render(request, 'tasks/addtask.html', {
		'task':tasks()
		})

