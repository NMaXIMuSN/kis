from django.urls import include, path, re_path

from .views import * 

urlpatterns = [
    path("questions/", QuestionListView.as_view()),
    path("answers/", SurveyAnswerListView.as_view()),
    path("user-list/", UserInfoView.as_view()),
    path("create-answer/", createAnswer),
    path("answers-list/", AnswersList.as_view()),
]
