from django.db import models

from users.models import Sustainer


class Post(models.Model):
    
    sustainer = models.ForeignKey(
        to=Sustainer,
        on_delete=models.CASCADE,
    )
    time = models.TimeField()
    text = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return f'{self.sustainer.user.first_name} {self.sustainer.user.last_name}\'s post'


class Commment(models.Model):
    
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    sustainer = models.ForeignKey(
        to=Sustainer,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        max_length=100,
    )
    
    
class Like(models.Model):
    
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    sustainer = models.ForeignKey(
        to=Sustainer,
        on_delete=models.CASCADE,
    )
    
