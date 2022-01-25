# Generated by Django 3.2.9 on 2021-12-16 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0024_auto_20211214_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Traditional', 'Traditional'), ('Contemporary', 'Contemporary'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks'), ('Dinner', 'Dinner'), ('Soup', 'Soup'), ('Carbs', 'Carbs')], default=None, max_length=255),
        ),
    ]