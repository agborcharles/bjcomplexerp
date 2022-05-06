# Generated by Django 4.0.4 on 2022-04-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boulangerie', '0002_boulangerieledger'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boulangerieledger',
            options={'verbose_name': 'Boulangerie Ledger', 'verbose_name_plural': 'Boulangerie Ledger'},
        ),
        migrations.AddField(
            model_name='boulangerieinventory',
            name='stock_status',
            field=models.CharField(blank=True, choices=[('Opening Stock', 'Opening Stock'), ('Closing Stock', 'Closing Stock')], default='', max_length=500, null=True, verbose_name='Sub Department'),
        ),
        migrations.AddField(
            model_name='boulangeriepurchases',
            name='stock_status',
            field=models.CharField(blank=True, choices=[('Purchases', 'Purchases')], default='', max_length=500, null=True, verbose_name='Sub Department'),
        ),
        migrations.AddField(
            model_name='boulangeriereturnsdamages',
            name='stock_status',
            field=models.CharField(blank=True, choices=[('Returns', 'Returns'), ('Damages', 'Damages')], default='', max_length=500, null=True, verbose_name='Sub Department'),
        ),
        migrations.AlterField(
            model_name='boulangerieinventory',
            name='department',
            field=models.CharField(blank=True, choices=[('Boulangerie', 'Boulangerie')], default='Boualangerie', max_length=500, null=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='boulangerieledger',
            name='department',
            field=models.CharField(blank=True, choices=[('Boulangerie', 'Boulangerie')], default='Boualangerie', max_length=500, null=True, verbose_name='Department'),
        ),
    ]
