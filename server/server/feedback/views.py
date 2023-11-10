from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import *
from .serializers import *

class QuestionListView(ListAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class SurveyAnswerListView(ListAPIView):
  queryset = SurveyAnswer.objects.all()
  serializer_class = SurveyAnswersSerializer

class UserInfoView(ListAPIView):
  queryset = UserInfo.objects.all()
  serializer_class = UserInfoSerializer

class AnswersList(ListAPIView):
  queryset = Answer.objects.all()
  serializer_class = AnswerExpandSerializer

@api_view(["POST"])
def createAnswer(request):
  req_body = json.loads(request.body)
  user_info = UserInfoSerializer(data=req_body["user"])

  if user_info.is_valid():
    user_info.save()

  answers = req_body["answers"]

  for ans in answers:
    ans["user_info"] = user_info.data["id"]
  
  answers_serialized = AnswerSerializer(data=answers, many=True)
  if answers_serialized.is_valid():
    answers_serialized.save()

  return Response(data={
    "user": user_info.data,
    "answers": answers_serialized.data
  })
