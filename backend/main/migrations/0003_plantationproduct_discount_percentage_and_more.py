# Generated by Django 4.2.6 on 2023-10-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_plantationproduct_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantationproduct',
            name='discount_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plantationproduct',
            name='tax_percentage',
            field=models.IntegerField(default=0),
        ),
    ]