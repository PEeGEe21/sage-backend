# Generated by Django 3.2.9 on 2021-12-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0018_product_featured_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]