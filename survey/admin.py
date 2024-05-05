from django.contrib import admin
from . import models

@admin.register(models.SentimentAnswer)
class SentimentAnswerAdmin(admin.ModelAdmin):
    list_display = ("user_id", "question_id", "question_variant", "sentiment", "importance")

# Register your models here.
# admin.site.register(models.SentimentAnswer, )
