# Generated by Django 3.0.6 on 2020-05-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200522_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kategori',
            field=models.CharField(default='Network', max_length=20),
        ),
    ]
