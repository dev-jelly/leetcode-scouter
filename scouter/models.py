from django.db import models
from django_extensions.db.models import TimeStampedModel


class Problem(TimeStampedModel):
    problem_number = models.IntegerField()
    title = models.CharField(max_length=180)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
