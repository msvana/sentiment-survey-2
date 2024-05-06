from django.contrib import admin
from . import models

@admin.register(models.SentimentAnswer)
class SentimentAnswerAdmin(admin.ModelAdmin):
    list_display = ("user_id", "question_id", "question_variant", "sentiment")

@admin.register(models.ImportanceAnswer)
class ImportanceAnswerAdmin(admin.ModelAdmin):
    list_display = ("user_id", "topic", "importance")
