# Generated by Django 3.1 on 2022-10-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20221012_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='is_payed',
            field=models.BooleanField(default=False),
        ),
    ]
