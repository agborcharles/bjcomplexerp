# Generated by Django 3.2.2 on 2022-04-06 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_ledger', '0004_auto_20220405_1646'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='general_accounting_ledger',
            new_name='GeneralLedger',
        ),
    ]