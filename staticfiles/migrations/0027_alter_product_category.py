# Generated by Django 3.2.9 on 2022-01-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0026_auto_20211217_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Local', 'Local'), ('Contemporary', 'Contemporary'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Fruits', 'Fruits'), ('Drinks', 'Drinks'), ('Dinner', 'Dinner'), ('Soup', 'Soup'), ('Stews', 'Stews'), ('Snacks', 'Snacks'), ('Porridge', 'Porridge'), ('Sauce', 'Sauce')], default=None, max_length=255),
        ),
    ]
