# Generated by Django 3.0.5 on 2021-11-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sage_main', '0002_auto_20211101_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='avatar-1.png', null=True, upload_to='category_image'),
        ),
    ]