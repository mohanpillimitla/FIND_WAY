from django.shortcuts import render,get_object_or_404
from .models import Timings,BusStation
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .forms import FindLocationForm
from django.utils import timezone

def displaybuses(request,id):
	queryset=Timings.objects.filter(bus_station_id=id).filter(arrival_time__lte=timezone.localtime(timezone.now()))
	return render(request,'buses/bus_view.html',{'form':queryset})
def findLocation(request):
	form=FindLocationForm()
	if request.method=="POST":

		form=FindLocationForm(request.POST or None)
		if form.is_valid():
			latitude=form.cleaned_data['latitude']
			longitude=form.cleaned_data['longitude']
			pnt=Point(latitude,longitude,srid=4328)
			queryset=BusStation.objects.annotate(distance=Distance(pnt,'location')).order_by('distance')[0:6]
			return render(request,'buses/location.html',{'form':queryset})
	return render(request,'buses/home.html',{'form':form})