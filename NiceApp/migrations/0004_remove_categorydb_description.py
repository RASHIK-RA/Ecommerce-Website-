# Generated by Django 4.2.1 on 2023-08-15 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NiceApp', '0003_productdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorydb',
            name='Description',
        ),
    ]
