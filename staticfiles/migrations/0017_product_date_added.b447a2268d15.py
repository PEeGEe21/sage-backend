# Generated by Django 3.2.9 on 2021-11-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0016_auto_20211105_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
