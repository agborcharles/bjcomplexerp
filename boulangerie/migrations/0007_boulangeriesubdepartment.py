# Generated by Django 4.0.4 on 2022-05-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boulangerie', '0006_boulangerieproducts_sessions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoulangerieSubDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_department', models.CharField(blank=True, choices=[('Boulangerie', 'Boulangerie'), ('Patisserie', 'Patisserie')], default='', max_length=500, null=True, verbose_name='Sub Department')),
            ],
            options={
                'verbose_name': 'Sub Department',
                'verbose_name_plural': 'Sub Departments',
            },
        ),
    ]