from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
