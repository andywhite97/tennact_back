# Generated by Django 5.2.4 on 2025-07-16 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='images',
        ),
    ]
