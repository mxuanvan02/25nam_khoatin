# Generated by Django 3.2 on 2021-04-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='year',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
