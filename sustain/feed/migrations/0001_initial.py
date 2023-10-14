# Generated by Django 4.2.6 on 2023-10-14 21:40


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.challenge')),
                ('sustainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sustainer')),
            ],
        ),
    ]
