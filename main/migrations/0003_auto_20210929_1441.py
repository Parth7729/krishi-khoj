# Generated by Django 3.2.7 on 2021-09-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tractordetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='tractordetails',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='tractordetails',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]