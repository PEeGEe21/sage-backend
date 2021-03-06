# Generated by Django 3.2.9 on 2021-11-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0008_product_deleted_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='favorite',
            new_name='is_favorite',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='recommended',
            new_name='is_recommended',
        ),
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Traditional', 'Traditional'), ('Contemporary', 'Contemporary'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks')], default=None, max_length=255),
        ),
    ]
