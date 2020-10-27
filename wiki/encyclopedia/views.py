from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import random

def index(request):
		return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})
def view(request,entry):


	data=util.get_entry(entry)
	return render(
		request, "encyclopedia/results.html", {'data':data,
		"md": markdown2.markdown(str(data)), 'ent':entry}
		)

def search(request):
	data=request.POST.get('q')
	lst=util.list_entries()
	matches=[]
	for i in lst:
		if str(data.upper())==str(i.upper()):
			return HttpResponseRedirect(reverse('view', kwargs={'entry':str(data)}))
		else:
			if data.upper() in i.upper():
				matches.append(i)
	return render(request, 'encyclopedia/index.html', {'entries':matches,'state':True})

def create(request):
	if request.method=='GET':
		return render(request, 'encyclopedia/create.html')
	else:
		title=request.POST.get('title')
		body=request.POST.get('body')

		lst=util.list_entries()
		for i in lst:
			if i.upper()==title.upper():
				return HttpResponse('Error: File with this title exists')
		util.save_entry(title,body)
		return HttpResponseRedirect(reverse('view', kwargs={'entry':title.upper()}))

def edit(request,data):
	title=data
	body=util.get_entry(title)
	if request.method=='GET':
		return render(request, 'encyclopedia/edit.html', {'title':title,'body':body})
	else:
		newtitle=request.POST.get('new-title')
		newbody=request.POST.get('new-body')
		util.save_entry(newtitle,newbody)
		return HttpResponseRedirect(reverse('index'))
def randm(request):
	lst=util.list_entries()
	rand=random.choice(lst)
	return HttpResponseRedirect(reverse('view', kwargs={'entry':rand}))


