# Generated by Django 4.0.4 on 2022-06-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0004_bakerymagazinedistribution_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakerymagazinedistribution',
            name='procuement_manager',
        ),
        migrations.RemoveField(
            model_name='bakerymagazinedistribution',
            name='purchase_id',
        ),
        migrations.RemoveField(
            model_name='bakerymagazinedistribution',
            name='supplier',
        ),
        migrations.AddField(
            model_name='bakerymagazinedistribution',
            name='distribution_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Distribution Id'),
        ),
        migrations.AddField(
            model_name='bakerymagazinedistribution',
            name='stock_manager',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Stock Manager'),
        ),
        migrations.AddField(
            model_name='bakerymagazinedistribution',
            name='sub_department',
            field=models.CharField(blank=True, choices=[('Boulangerie Morning', 'Boulangerie Morning'), ('Boulangerie Evening', 'Boulangerie Evening'), ('Patisserie Morning', 'Patisserie Morning'), ('Patisserie Evening', 'Patisserie Evening')], default='', max_length=500, null=True, verbose_name='Sub Department'),
        ),
        migrations.AddField(
            model_name='bakerymagazinedistribution',
            name='sub_department_manager',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Sub Department Manager'),
        ),
        migrations.AlterField(
            model_name='bakerypurchase',
            name='category',
            field=models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='Direct', max_length=500, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='bakerypurchase',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Location'),
        ),
    ]