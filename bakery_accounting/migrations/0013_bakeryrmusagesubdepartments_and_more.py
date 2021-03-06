# Generated by Django 4.0.4 on 2022-06-21 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0012_remove_bakeryinventorysubdepartments_direct_indirect_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryRmUsageSubDepartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('sub_department', models.CharField(blank=True, choices=[('Boulangerie Morning', 'Boulangerie Morning'), ('Boulangerie Evening', 'Boulangerie Evening'), ('Patisserie Morning', 'Patisserie Morning'), ('Patisserie Evening', 'Patisserie Evening'), ('All', 'All')], default='', max_length=500, null=True, verbose_name='Sub Department')),
                ('status', models.CharField(blank=True, default='Rm Usage', max_length=500, null=True, verbose_name='Status')),
                ('session', models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='', max_length=500, null=True, verbose_name='Sub Department')),
                ('mixture_number', models.CharField(blank=True, choices=[('First Mixture', 'First Mixture'), ('Second Mixture', 'Second Mixture'), ('Third Mixture', 'Third Mixture'), ('Fourth Mixture', 'Fourth Mixture'), ('Fifth Mixture', 'Fifth Mixture'), ('Sixth Mixture', 'Sixth Mixture'), ('Seventh Mixture', 'Seventh Mixture'), ('Eight Mixture', 'Eight Mixture'), ('Ninth Mixture', 'Ninth Mixture'), ('Tenth Mixture', 'Tenth Mixture'), ('Eleventh Mixture', 'Eleventh Mixture')], default='', max_length=500, null=True, verbose_name='Mixture Number')),
                ('supervisor', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Supervisor')),
                ('product', models.CharField(max_length=200, verbose_name='Product')),
                ('category', models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='', max_length=500, null=True, verbose_name='Category')),
                ('weight_per_pack', models.FloatField(default=0.0, verbose_name='Weight / Pack')),
                ('entry_measure', models.CharField(blank=True, choices=[('Grams', 'Grams'), ('Kg', 'Kg'), ('Unit', 'Unit'), ('Litre', 'Litre')], default='', max_length=500, null=True, verbose_name='Entry Measure')),
                ('qty', models.FloatField(default=0.0, verbose_name='Quantity')),
                ('rm_total_weight_grams', models.FloatField(default=0.0, verbose_name='RM Total Weight (Grams)')),
                ('unit_cost_price', models.FloatField(default=0.0, verbose_name='Unit Cost Price')),
                ('total_cost_price', models.FloatField(default=0.0, verbose_name='Total Cost Price')),
            ],
            options={
                'verbose_name': 'Bakery Raw Material Usage Sub-Departments',
                'verbose_name_plural': 'Bakery Raw Material Usage Sub-Departments',
            },
        ),
        migrations.AlterModelOptions(
            name='bakeryinventorysubdepartments',
            options={},
        ),
        migrations.AlterField(
            model_name='bakeryinventorysubdepartments',
            name='stock_status',
            field=models.CharField(blank=True, choices=[('Opening Stock', 'Opening Stock'), ('Closing Stock', 'Closing Stock'), ('Returns', 'Returns'), ('Transfer Inwards', 'Transfer Inwards'), ('Transfer Outwards', 'Transfer Outwards'), ('Damages', 'Damages'), ('Added Stock', 'Added Stock')], default='', max_length=500, null=True, verbose_name='Stock Status'),
        ),
    ]
