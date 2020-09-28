from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse

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
		if str(data.upper())==str(i):
			return HttpResponseRedirect(reverse('view', kwargs={'entry':str(data.upper())}))
		else:
			if data.upper() in i.upper():
				matches.append(i.upper())
	return render(request, 'encyclopedia/index.html', {'entries':matches,'state':True})

	

