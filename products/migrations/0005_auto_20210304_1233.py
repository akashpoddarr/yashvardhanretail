# Generated by Django 3.1.7 on 2021-03-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
