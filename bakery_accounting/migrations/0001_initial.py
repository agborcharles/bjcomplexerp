# Generated by Django 4.0.4 on 2022-05-31 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('customer', models.CharField(blank=True, max_length=500, null=True, verbose_name='Customers')),
                ('busness_type', models.CharField(blank=True, choices=[('Random Customer', 'Random Customer'), ('Others', 'Others'), ('Company', 'Company'), ('Sole Proprietor', 'Sole Proprietor'), ('Supplier', 'Supplier'), ('Institutions', 'Institutions')], max_length=500, null=True, verbose_name='busness_type')),
                ('quarter', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='quarter')),
                ('street', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='street')),
                ('gps_long', models.FloatField(blank=True, default='', max_length=500, null=True, verbose_name='gps_long')),
                ('gps_lat', models.FloatField(blank=True, default='', max_length=500, null=True, verbose_name='gps_lat')),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Address')),
                ('phone_1', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='phone_1')),
                ('phone_2', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='phone_2')),
                ('road_street_location', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Road Street Location')),
            ],
            options={
                'verbose_name': 'Bakery Customers',
                'verbose_name_plural': 'Bakery Customers',
            },
        ),
        migrations.CreateModel(
            name='BakeryInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('sub_department', models.CharField(blank=True, choices=[('Boulangerie Morning', 'Boulangerie Morning'), ('Boulangerie Evening', 'Boulangerie Evening'), ('Patisserie', 'Patisserie')], default='', max_length=500, null=True, verbose_name='Sub Department')),
                ('stock_status', models.CharField(blank=True, choices=[('Opening Stock', 'Opening Stock'), ('Closing Stock', 'Closing Stock')], default='', max_length=500, null=True, verbose_name='Stock Status')),
                ('direct_indirect', models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='', max_length=500, null=True, verbose_name='Drect / Indirect')),
                ('entry_measure', models.CharField(blank=True, choices=[('Grams', 'Grams'), ('Kg', 'Kg'), ('Unit', 'Unit'), ('Litre', 'Litre')], default='', max_length=500, null=True, verbose_name='Entry Measure')),
                ('weight_per_pack', models.FloatField(default=0.0, verbose_name='Weight / Pack')),
                ('product', models.CharField(max_length=200, verbose_name='Product')),
                ('qty', models.FloatField(default=0.0, verbose_name='Quantity')),
                ('unit_cost_price', models.FloatField(default=0.0, verbose_name='Unit Cost Price')),
                ('total_cost_price', models.FloatField(default=0.0, verbose_name='Total Cost Price')),
            ],
            options={
                'verbose_name': 'Bakery Inventory',
                'verbose_name_plural': 'Bakery Inventory',
            },
        ),
        migrations.CreateModel(
            name='BakeryOpeningBalances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('openingbalance_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Opening Balance Id')),
                ('customer', models.CharField(max_length=200, verbose_name='Customer')),
                ('total_amount', models.FloatField(default=0.0, verbose_name='Amount')),
            ],
            options={
                'verbose_name': 'Bakery Opening Balance',
                'verbose_name_plural': 'Bakery Opening Balances',
            },
        ),
        migrations.CreateModel(
            name='BakeryPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('quarter', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Quarter')),
                ('street', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Street')),
                ('session', models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='', max_length=500, null=True, verbose_name='Session')),
                ('collector', models.CharField(blank=True, choices=[('Moses', 'Moses'), ('Glory', 'Glory'), ('Kesty', 'Kesty'), ('Charles', 'Charles'), ('Cyril', 'Cyril'), ('Aly', 'Aly'), ('Joan', 'Joan'), ('Micheal', 'Micheal'), ('Esther', 'Esther'), ('Violet', 'Violet'), ('Kaba', 'Kaba'), ('Brenda', 'Brenda')], max_length=500, null=True, verbose_name='Collector')),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Payment Invoice Id')),
                ('customer', models.CharField(max_length=200, verbose_name='Customer')),
                ('amount', models.FloatField(default=0.0, verbose_name='Amount')),
                ('payment_mode', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Mobile Money', 'Mobile Money'), ('Bank', 'Bank'), ('Cheque', 'Cheque')], default='', max_length=200, null=True, verbose_name='Payment Mode')),
            ],
            options={
                'verbose_name': 'Bakery Payment',
                'verbose_name_plural': 'Bakery Payments',
            },
        ),
        migrations.CreateModel(
            name='BakeryPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('procuement_manager', models.CharField(max_length=200, verbose_name='Procuement Manager')),
                ('purchase_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Purchase Invoice Id')),
                ('supplier', models.CharField(max_length=200, verbose_name='Supplier')),
                ('category', models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='Direct', max_length=500, null=True, verbose_name='Category')),
                ('entry_measure', models.CharField(max_length=200, verbose_name='Entry Measure')),
                ('weight_pack', models.CharField(max_length=200, verbose_name='Weight/Pack')),
                ('product', models.CharField(max_length=200, verbose_name='Product')),
                ('qty', models.FloatField(default=0.0, verbose_name='Quantity')),
                ('unit_cost_price', models.FloatField(default=0.0, verbose_name='Unit Cost Price')),
                ('total_cost_price', models.FloatField(default=0.0, verbose_name='Total Cost Price')),
            ],
            options={
                'verbose_name': 'Bakery Purchase',
                'verbose_name_plural': 'Bakery Purchases',
            },
        ),
        migrations.CreateModel(
            name='BakeryReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('return_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Return Invoice Id')),
                ('invoice_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Invoice Id')),
                ('customer_from', models.CharField(max_length=200, verbose_name='Customer_from')),
                ('customer_to', models.CharField(max_length=200, verbose_name='Customer_to')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('sub_department', models.CharField(blank=True, choices=[('Boulangerie', 'Boulangerie'), ('Patisserie', 'Patisserie')], default='Bakery', max_length=500, null=True, verbose_name='Sub Department')),
                ('category', models.CharField(blank=True, choices=[('Bread', 'Bread'), ('Confectionary', 'Confectionary'), ('Hamburger', 'Hamburger'), ('Sandwich', 'Sandwich'), ('Cake', 'Cake'), ('Milk Bread', 'Milk Bread'), ('Biscuit', 'Biscuit'), ('Croissant', 'Croissant'), ('Fruitage', 'Fruitage')], default='', max_length=500, null=True)),
                ('product', models.CharField(max_length=200, verbose_name='Product Name')),
                ('qty', models.FloatField(verbose_name='Quantity')),
                ('cost_price', models.FloatField(default=0.0, verbose_name='Cost Price')),
                ('total_amount', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'Bakery Returns',
                'verbose_name_plural': 'Bakery Returns',
            },
        ),
        migrations.CreateModel(
            name='BakeryRmDamages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('damage_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Purchase Invoice Id')),
                ('category', models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='Direct', max_length=500, null=True, verbose_name='Category')),
                ('entry_measure', models.CharField(max_length=200, verbose_name='Entry Measure')),
                ('weight_pack', models.CharField(max_length=200, verbose_name='Weight/Pack')),
                ('product', models.CharField(max_length=200, verbose_name='Product')),
                ('qty', models.FloatField(default=0.0, verbose_name='Quantity')),
                ('unit_cost_price', models.FloatField(default=0.0, verbose_name='Unit Cost Price')),
                ('total_cost_price', models.FloatField(default=0.0, verbose_name='Total Cost Price')),
            ],
            options={
                'verbose_name': 'Bakery Raw Material Damage',
                'verbose_name_plural': 'Bakery Raw Material Damages',
            },
        ),
        migrations.CreateModel(
            name='BakeryRmReturns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('return_manager', models.CharField(max_length=200, verbose_name='Procuement Manager')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('return_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Purchase Invoice Id')),
                ('supplier', models.CharField(max_length=200, verbose_name='Supplier')),
                ('category', models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='Direct', max_length=500, null=True, verbose_name='Category')),
                ('entry_measure', models.CharField(max_length=200, verbose_name='Entry Measure')),
                ('weight_pack', models.CharField(max_length=200, verbose_name='Weight/Pack')),
                ('product', models.CharField(max_length=200, verbose_name='Product')),
                ('qty', models.FloatField(default=0.0, verbose_name='Quantity')),
                ('unit_cost_price', models.FloatField(default=0.0, verbose_name='Unit Cost Price')),
                ('total_cost_price', models.FloatField(default=0.0, verbose_name='Total Cost Price')),
            ],
            options={
                'verbose_name': 'Bakery Raw Material Return',
                'verbose_name_plural': 'Bakery Raw Material Returns',
            },
        ),
        migrations.CreateModel(
            name='BakerySales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('order_no', models.IntegerField()),
                ('invoice_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Invoice Id')),
                ('supplier', models.CharField(blank=True, choices=[('Moses', 'Moses'), ('Glory', 'Glory'), ('Kesty', 'Kesty')], default='', max_length=500, null=True, verbose_name='Supplier')),
                ('customer', models.CharField(max_length=200, verbose_name='Customer')),
                ('department', models.CharField(blank=True, choices=[('Bakery', 'Bakery')], default='Bakery', max_length=500, null=True, verbose_name='Department')),
                ('sub_department', models.CharField(blank=True, choices=[('Boulangerie', 'Boulangerie'), ('Patisserie', 'Patisserie')], default='Bakery', max_length=500, null=True, verbose_name='Sub Department')),
                ('category', models.CharField(blank=True, choices=[('Bread', 'Bread'), ('Confectionary', 'Confectionary'), ('Hamburger', 'Hamburger'), ('Sandwich', 'Sandwich'), ('Cake', 'Cake'), ('Milk Bread', 'Milk Bread'), ('Biscuit', 'Biscuit'), ('Croissant', 'Croissant'), ('Fruitage', 'Fruitage')], default='', max_length=500, null=True)),
                ('session', models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='', max_length=500, null=True, verbose_name='Session')),
                ('product', models.CharField(max_length=200, verbose_name='Product Name')),
                ('qty', models.FloatField(default=0.0, verbose_name='Quantity')),
                ('cost_price', models.FloatField(default=0.0, verbose_name='Cost Price')),
                ('total_amount', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0, verbose_name='Discount')),
                ('discount_value', models.FloatField(default=0.0, verbose_name='Discount Value')),
                ('net_amount', models.FloatField(default=0.0, verbose_name='Net Amount')),
                ('commission', models.FloatField(default=0.0, verbose_name='Commission')),
            ],
            options={
                'verbose_name': 'Bakery Sales',
                'verbose_name_plural': 'Bakery Sales',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Cquarter_name')),
            ],
            options={
                'verbose_name': 'Quarter',
                'verbose_name_plural': 'Quarter',
            },
        ),
    ]
