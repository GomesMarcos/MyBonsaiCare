# Generated by Django 3.1.4 on 2021-01-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_auto_20210103_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='observations',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
