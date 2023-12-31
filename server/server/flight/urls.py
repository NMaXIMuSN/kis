from django.urls import include, path, re_path

from flight.views import SchedulesListView, AirportListView, CancelFlightView, UploadFileView, ScheduleEditView, SchedulesListViewReturn

urlpatterns = [
    path("schedules_list/", SchedulesListView.as_view()),
    path("schedules_list_return/", SchedulesListViewReturn.as_view()),
    # path("schedules_list_return/", insert_list),
    path("schedule_cancel/<int:pk>", CancelFlightView.as_view()),
    path("airport_list", AirportListView.as_view()),
    path("schedule_edit/<int:pk>", ScheduleEditView.as_view()),
    re_path(r'^upload_file/(?P<filename>[^/]+)$', UploadFileView.as_view()),
]
