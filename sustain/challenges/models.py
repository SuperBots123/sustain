from django.db import models
from users.models import Sustainer

class Challenge(models.Model):
    sustainer = models.ForeignKey(Sustainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    # add other fields as needed
