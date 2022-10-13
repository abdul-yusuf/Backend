# Generated by Django 3.1 on 2022-10-12 16:58

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marchant', '0003_auto_20221012_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_product',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.fields.AutoField, to='marchant.rating'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.fields.AutoField, to='marchant.rating'),
        ),
    ]
