from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
		return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})
def rand(request,entry):

	data=util.get_entry(entry)
	return render(
		request, "encyclopedia/results.html", {'data':util.get_entry(entry),
		"md": markdown2.markdown(str(data))}
		)

def searchh(request):
	if request.method=='POST':
		
		data=request.POST.get('q')
		if (util.get_entry(data)) is not None:
			return HttpResponseRedirect(reverse("rand", kwargs={'entry':data}))
		else:
			lst=util.list_entries()
			matches=[]
			for i in lst:
			#if data==i:
				#matches.append(data)
				if data.upper() in i.upper():
					matches.append(i)
					return render(request, "encyclopedia/index.html", {
						"entries": matches,
						'search':True,
						'value':data})
	

