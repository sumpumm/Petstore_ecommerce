# Generated by Django 5.1.3 on 2024-12-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0004_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]
