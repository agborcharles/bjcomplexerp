# Generated by Django 3.2.2 on 2022-04-08 14:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0053_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('8ce8b577-2b9c-4694-ad9a-773a9c3242ac'), max_length=500, null=True),
        ),
    ]