from django.urls import include, path, re_path

from .views import TicketsAddView, TicketsListView, AmenitiesListView,AmenitiesGetListByPkView, TicketsAmenitiesView, amenitiesStats, AmenitiesCabinTypeListView

urlpatterns = [
    path("/add", TicketsAddView.as_view()),
    path("/list", TicketsListView.as_view()),
    path("/amenities", AmenitiesListView.as_view()),
    path("/amenities/cabin_type", AmenitiesCabinTypeListView.as_view()),
    path("/amenities/<int:pk>", AmenitiesGetListByPkView.as_view()),
    path("/amenities/add", TicketsAmenitiesView.as_view()),
    path("/amenities/stats", amenitiesStats),
]
