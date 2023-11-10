from django.urls import include, path, re_path

from .views import FlightView

urlpatterns = [
  path('/flight', FlightView)
]
