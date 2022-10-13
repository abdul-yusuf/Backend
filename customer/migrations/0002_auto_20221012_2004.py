# Generated by Django 3.1 on 2022-10-12 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='product',
        ),
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='authorization',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='is_payed',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='payment',
            name='ref_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]