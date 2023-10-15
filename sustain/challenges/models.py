from django.db import models
from users.models import Sustainer


class Challenge(models.Model):
    cause = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
    )
    points = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )
    time = models.DateTimeField(
        null=True,
        blank=True,
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
    )
    completionStatus = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    sustainer = models.ForeignKey(
        to=Sustainer,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='challenge_images/',
        null=True,
        blank=True,
    )
    def __str__(self):
        return f"{self.cause}, {self.description}, {self.points}, {self.time}, {self.completionStatus}, {self.sustainer}"
