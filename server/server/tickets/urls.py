from django.urls import include, path, re_path

from .views import TicketsAddView

urlpatterns = [
    path("/add", TicketsAddView.as_view()),
]
