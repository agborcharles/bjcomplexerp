# Generated by Django 3.2.2 on 2022-04-11 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0022_auto_20220410_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bakeryinventory',
            options={'verbose_name': 'Bakery Inventory', 'verbose_name_plural': 'Bakery Inventory'},
        ),
        migrations.AlterModelOptions(
            name='bakeryopeningbalances',
            options={'verbose_name': 'Bakery Opening Balance', 'verbose_name_plural': 'Bakery Opening Balances'},
        ),
        migrations.AlterModelOptions(
            name='bakerypayment',
            options={'verbose_name': 'Bakery Payment', 'verbose_name_plural': 'Bakery Payments'},
        ),
        migrations.AlterModelOptions(
            name='bakerypurchase',
            options={'verbose_name': 'Bakery Purchase', 'verbose_name_plural': 'Bakery Purchases'},
        ),
        migrations.AlterModelOptions(
            name='bakeryreturn',
            options={'verbose_name': 'Bakery Returns', 'verbose_name_plural': 'Bakery Returns'},
        ),
        migrations.AlterModelOptions(
            name='bakeryrmdamages',
            options={'verbose_name': 'Bakery Raw Material Damage', 'verbose_name_plural': 'Bakery Raw Material Damages'},
        ),
        migrations.AlterModelOptions(
            name='bakeryrmreturns',
            options={'verbose_name': 'Bakery Raw Material Return', 'verbose_name_plural': 'Bakery Raw Material Returns'},
        ),
        migrations.AlterModelOptions(
            name='bakerysales',
            options={'verbose_name': 'Bakery Sales', 'verbose_name_plural': 'Bakery Sales'},
        ),
    ]