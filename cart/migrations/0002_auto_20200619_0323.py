# Generated by Django 3.0.6 on 2020-06-19 03:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
