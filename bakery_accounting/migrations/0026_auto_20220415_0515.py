# Generated by Django 3.2.2 on 2022-04-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0025_auto_20220415_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakerycustomers',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='bakerycustomers',
            name='gps_lat',
            field=models.FloatField(blank=True, default='', max_length=500, null=True, verbose_name='gps_lat'),
        ),
        migrations.AlterField(
            model_name='bakerycustomers',
            name='gps_long',
            field=models.FloatField(blank=True, default='', max_length=500, null=True, verbose_name='gps_long'),
        ),
    ]