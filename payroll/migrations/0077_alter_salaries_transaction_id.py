# Generated by Django 4.0.4 on 2022-04-30 18:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0076_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('b64d7777-1377-4953-98a1-a499ae295c0d'), max_length=500, null=True),
        ),
    ]
