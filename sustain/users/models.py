from django.db import models
from django.contrib.auth.models import User


class Sustainer(models.Model):
    
    STATE_CHOICES = [
        ('GA', 'Georgia'),
    ]
    
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    about = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )
    joined = models.DateField(
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    state = models.CharField(
        choices=STATE_CHOICES,
        max_length=25,
        null=True,
        blank=True,
    )
    linked_in = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    following = models.ManyToManyField(
        to='self', 
        related_name='followers', 
        symmetrical=False,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    
