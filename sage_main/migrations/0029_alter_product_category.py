# Generated by Django 4.0.1 on 2022-01-25 01:30

from django.db import migrations, models
import sage_main.models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0028_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default=None, max_length=255, verbose_name=sage_main.models.Category),
        ),
    ]