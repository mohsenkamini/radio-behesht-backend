from django.urls import path
from .views import StreamRequestView

urlpatterns = [
    path('api/stream/request', StreamRequestView.as_view(), name='stream-request'),
]
