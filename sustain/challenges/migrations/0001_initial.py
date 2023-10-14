from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Challenge",
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('points', models.IntegerField(default=0)),
                ('time', models.DateField(auto_now_add=True)),
                ('completionStatus', models.BooleanField(default=False)),
                # ('latitude', models.FloatField()),
                # ('longitude', models.FloatField()),
                ('sustainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.sustainer')),
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cause", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=1000)),
                ("points", models.IntegerField(default=0)),
                ("time", models.DateField(auto_now_add=True)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("completionStatus", models.BooleanField(default=False)),
                (
                    "sustainer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.sustainer",
                    ),
                ),
            ],
        ),
    ]