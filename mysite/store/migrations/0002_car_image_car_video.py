# Generated by Django 5.1.2 on 2024-10-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vid/'),
        ),
        migrations.AddField(
            model_name='car',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='vid/'),
        ),
    ]
