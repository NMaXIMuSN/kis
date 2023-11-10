from rest_framework import serializers

from .models import *
from flight.models import Airport


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class SurveyAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = "__all__"

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class AnswerExpandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

    user_info = UserInfoSerializer()
    question = QuestionSerializer()
    survey_answer = SurveyAnswersSerializer()
