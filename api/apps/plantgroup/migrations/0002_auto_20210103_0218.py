# Generated by Django 3.1.4 on 2021-01-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantgroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantgroup',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
