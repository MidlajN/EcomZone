# Generated by Django 4.1.3 on 2022-12-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0003_alter_product_prod_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(upload_to='product'),
        ),
    ]
