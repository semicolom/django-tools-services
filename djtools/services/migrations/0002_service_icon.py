# Generated by Django 2.1.4 on 2018-12-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djtools.services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='services'),
        ),
    ]
