from django.urls import path
from .views import StationListView

urlpatterns = [
    path('api/radio/stations/', StationListView.as_view(), name='station-list'),
]
