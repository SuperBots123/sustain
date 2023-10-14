from django.db import models
from challenges.models import Challenge
from users.models import Sustainer
    
    
class Like(models.Model):
    
    post = models.ForeignKey(
        to=Challenge,
        on_delete=models.CASCADE,
    )
    sustainer = models.ForeignKey(
        to=Sustainer,
        on_delete=models.CASCADE,
    )
    
