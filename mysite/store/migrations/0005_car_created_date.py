# Generated by Django 5.1.2 on 2024-10-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_car_title_remove_car_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]