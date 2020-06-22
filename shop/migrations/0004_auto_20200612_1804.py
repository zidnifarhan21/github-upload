# Generated by Django 3.0.6 on 2020-06-12 18:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999999)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='kategori',
            field=models.CharField(choices=[('NW', 'Network'), ('DB', 'Database'), ('PM', 'Programming'), ('ML', 'Machine Learning')], default='Network', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='tahun',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
