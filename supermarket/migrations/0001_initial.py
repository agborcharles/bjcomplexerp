# Generated by Django 3.2.2 on 2022-04-07 08:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupermarketSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, default='Supermarket', max_length=500, null=True, verbose_name='Department')),
                ('session', models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='', max_length=500, null=True, verbose_name='Session')),
                ('sales_person', models.CharField(max_length=200, verbose_name='Sales Person')),
                ('category', models.CharField(blank=True, max_length=200, null=True, verbose_name='Category')),
                ('product', models.CharField(max_length=200, verbose_name='Product')),
                ('qty', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Quantity')),
                ('unit_cost_price', models.FloatField(default=0.0, verbose_name='Unit Cost Price')),
                ('unit_selling_price', models.FloatField(default=0.0, verbose_name='Unit Selling Price')),
                ('total_cost_price', models.FloatField(default=0.0, verbose_name='Total Cost Price')),
                ('total_selling_price', models.FloatField(default=0.0, verbose_name='Total Selling Price')),
                ('gross_profit', models.FloatField(default=0.0, verbose_name='Gross Profit')),
                ('margin', models.FloatField(default=0.0, verbose_name='margin')),
            ],
            options={
                'verbose_name': 'Supermarket Sales',
                'verbose_name_plural': 'Supermarket Sales',
            },
        ),
    ]