from django.shortcuts import render
import markdown2
from . import util


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
	data=request.GET.get('q', '')

	if (util.get_entry(data)) is not None:
		return HttpResponseRedirect(reverse("rand", kwargs={'entry':data}))
	else:
		lst=util.list_entries()
		matches=[]
		for i in lst:
			if data==i:
				matches.append(data)
			elif data in i:
				matches.append(data)
		return render(request, "encyclopedia/index.html", {"entries": matches})
	

