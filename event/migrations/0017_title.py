# Generated by Django 3.2 on 2021-04-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0016_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]