from django.urls import path
from . import views

urlpatterns = [
    # ex: /pollls/
    path("", views.index, name="index"),
    # ex: /polls/<num>/
    path("<int:question_id>", views.detail , name="results"),
    # ex: /polls/<num>/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/<num>/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]