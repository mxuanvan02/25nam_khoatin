# Generated by Django 3.2 on 2021-04-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_alter_mailadmin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
