# Generated by Django 4.0.4 on 2022-04-28 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boulangerie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoulangerieLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('session', models.CharField(blank=True, choices=[('1st Session', '1st Session'), ('2nd Session', '2nd Session')], default='', max_length=500, null=True, verbose_name='Session')),
                ('department', models.CharField(blank=True, choices=[('Boulangerie', 'Boulangerie'), ('Patisserie', 'Patisserie')], default='Boualangerie', max_length=500, null=True, verbose_name='Department')),
                ('employee', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Employee')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('accounts_dr', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Account Debit')),
                ('accounts_cr', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='AccountsCredit')),
            ],
            options={
                'verbose_name': 'Boulangerie Inventory',
                'verbose_name_plural': 'Boulangerie Inventory',
            },
        ),
    ]