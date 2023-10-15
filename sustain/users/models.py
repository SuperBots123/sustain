from django.db import models
from django.contrib.auth.models import User


class Sustainer(models.Model):
    
    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Conneticut'),
        ('DC', 'District of Columbia'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Lousiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennslyvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennesee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virgina'),
        ('WA', 'Washington'),
        ('WV', 'West Virgina'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')

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
    points = models.IntegerField(
        default=0,
    )
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    
