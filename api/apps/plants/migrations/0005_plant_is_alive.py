# Generated by Django 3.1.4 on 2021-01-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_plant_observations'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='is_alive',
            field=models.BooleanField(default=True),
        ),
    ]
