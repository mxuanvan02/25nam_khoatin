# Generated by Django 3.2 on 2021-04-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_image_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
