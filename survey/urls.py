from django.urls import path

from . import views

urlpatterns = [
    path("", views.question, name="question"),
    path("submit/", views.submit, name="submit"),
    path("importance/", views.importance, name="importance"),
    path("submit/importance/", views.submit_importance, name="submit_importance"),
    path("reset/", views.reset, name="reset"),
    path("end/", views.end, name="end"),
]
