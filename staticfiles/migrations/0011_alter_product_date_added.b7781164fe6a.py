# Generated by Django 3.2.9 on 2021-11-04 01:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0010_alter_product_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
