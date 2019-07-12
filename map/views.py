from django.shortcuts import render
from map.models import Route, Station

# Create your views here.
def stations_views(request):
	context = {}
	if request.method == 'GET':

		if 'route' in request.GET:
			route = request.GET['route']

			stations = Route.objects.get(name=route).stations.all()
			stations_lat = Route.objects.get(name=route).stations.all() \
				.order_by('latitude')
			stations_long = Route.objects.get(name=route).stations.all() \
				.order_by('longitude')

			y = (stations_lat.first().latitude + stations_lat.last().latitude) / 2
			x = (stations_long.first().longitude + stations_long.last().longitude) / 2

			center = {'x':x,'y':y}

			context['routes'] = Route.objects.all()
			context['route'] = route
			context['stations'] = stations
			context['center'] = center
		else:
			context['routes'] = Route.objects.all()

	return render(request, 'stations.html', context)
