from django.db import models
from users.models import Sustainer

# Create your models here.
class Challenge(models.Model):
    cause = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    points = models.IntegerField(default=0)
    time = models.DateField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    completionStatus = models.BooleanField(default=False)
    sustainer = models.ForeignKey(
        to=Sustainer,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return f"{self.cause}, {self.description}, {self.points}, {self.time}, {self.completionStatus}, {self.sustainer}"
