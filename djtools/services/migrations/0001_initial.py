# Generated by Django 2.1.2 on 2018-10-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services')),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('featured', models.BooleanField(db_index=True, default=False)),
                ('order', models.IntegerField(db_index=True, default=0)),
            ],
            options={
                'ordering': ('-featured', 'order'),
                'abstract': False,
            },
        ),
        migrations.AlterIndexTogether(
            name='service',
            index_together={('featured', 'order'), ('active', 'featured', 'order')},
        ),
    ]
