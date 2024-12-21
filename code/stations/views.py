from django.shortcuts import render
from django.http import JsonResponse
from .models import Station
from django.views import View
# Create your views here.

class StationListView(View):
    def get(self, request):
        stations = Station.objects.all()
        station_data = [{"id": station.id, "name": station.name, "stream_url": f"/media/radio/{station.name}/"} for station in stations]
        return JsonResponse(station_data, safe=False)

