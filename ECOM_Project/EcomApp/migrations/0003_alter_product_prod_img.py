# Generated by Django 4.1.3 on 2022-12-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.FileField(upload_to='product'),
        ),
    ]
