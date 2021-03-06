# Generated by Django 3.2.9 on 2021-12-07 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0021_auto_20211204_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Traditional', 'Traditional'), ('Contemporary', 'Contemporary'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks'), ('Dinner', 'Dinner'), ('Soup', 'Soup')], default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sage_main.product'),
        ),
    ]
