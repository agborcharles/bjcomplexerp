# Generated by Django 4.0.4 on 2022-06-17 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0010_alter_bakerypurchase_stock_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BakeryRmReturns',
            new_name='BakeryRawMaterialUsage',
        ),
        migrations.AlterModelOptions(
            name='bakeryrawmaterialusage',
            options={'verbose_name': 'Bakery Raw Material Usage', 'verbose_name_plural': 'Bakery Raw Material Usage'},
        ),
    ]
