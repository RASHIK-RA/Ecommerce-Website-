# Generated by Django 4.2.1 on 2023-09-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_userdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
