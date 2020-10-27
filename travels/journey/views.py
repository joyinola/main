from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
	return render(request,'journey/index.html', {'trips':models.Travel.objects.all()})

def flight(request,flight_id):
	f=models.Travel.objects.get(id=flight_id)
	p=f.passengers.all()
	np=models.Passengers.objects.exclude(flight=f)


	return render(request, 'journey/flights.html', {
		'flight':f, 'passengers':p, 'non_passengers':np})
def book(request,flight_id):
	if request.method=='POST':
		f=models.Travel.objects.get(id=flight_id)

		p_id=request.POST.get('passengers')
		p=models.Passengers.objects.get(id=p_id)
		fp=p.flight.add(f)
		return HttpResponseRedirect(reverse('journey:flight', args=(f.id,)))

