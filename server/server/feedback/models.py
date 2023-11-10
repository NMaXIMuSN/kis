from django.db import models
from django.utils import timezone

class SurveyAnswer(models.Model):
  value = models.IntegerField()
  title = models.CharField(max_length=255)

class UserInfo(models.Model):
  going_from = models.ForeignKey("flight.Airport", on_delete=models.CASCADE, related_name="going_from", blank=True)
  going_to = models.ForeignKey("flight.Airport", on_delete=models.CASCADE, related_name="going_to", blank=True)
  age = models.IntegerField(blank=True)
  gender = models.CharField(max_length=30, blank=True)
  cabin_type = models.CharField(max_length=30, blank=True)

class Answer(models.Model):
  question = models.ForeignKey("feedback.Question", on_delete=models.CASCADE)
  user_info = models.ForeignKey("feedback.UserInfo", on_delete=models.CASCADE)
  survey_answer = models.ForeignKey("feedback.SurveyAnswer", on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=timezone.now)

class Question(models.Model):
  title = models.CharField(max_length=255)