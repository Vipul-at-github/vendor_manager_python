# Generated by Django 2.2.18 on 2023-12-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendmangr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.DurationField(),
        ),
    ]
