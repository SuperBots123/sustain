# Generated by Django 4.2.1 on 2023-10-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_sustainer_city_alter_sustainer_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='sustainer',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='users.sustainer'),
        ),
    ]