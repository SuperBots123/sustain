# Generated by Django 4.2.6 on 2023-10-14 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sustainer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("about", models.TextField(blank=True, max_length=300, null=True)),
                ("joined", models.DateField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=25, null=True)),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AL", "Alabama"),
                            ("AK", "Alaska"),
                            ("AZ", "Arizona"),
                            ("AR", "Arkansas"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Conneticut"),
                            ("DC", "District of Columbia"),
                            ("DE", "Delaware"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("HI", "Hawaii"),
                            ("ID", "Idaho"),
                            ("IL", "Illinois"),
                            ("IN", "Indiana"),
                            ("IA", "Iowa"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Lousiana"),
                            ("ME", "Maine"),
                            ("MD", "Maryland"),
                            ("MA", "Massachusetts"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MS", "Mississippi"),
                            ("MO", "Missouri"),
                            ("MT", "Montana"),
                            ("NE", "Nebraska"),
                            ("NV", "Nevada"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NY", "New York"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennslyvania"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennesee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VT", "Vermont"),
                            ("VA", "Virgina"),
                            ("WA", "Washington"),
                            ("WV", "West Virgina"),
                            ("WI", "Wisconsin"),
                            ("WY", "Wyoming"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                ("linked_in", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="followers",
                        to="users.sustainer",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
