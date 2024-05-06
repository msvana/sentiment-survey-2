from django.db import models


class SentimentAnswer(models.Model):
    user_id = models.UUIDField()
    question_id = models.IntegerField()
    question_variant = models.IntegerField()
    question_text = models.TextField()
    sentiment = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ImportanceAnswer(models.Model):
    user_id = models.UUIDField()
    topic = models.TextField()
    importance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
