# Generated by Django 2.2.6 on 2019-10-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldborder',
            name='worldborder_slug',
            field=models.SlugField(blank=True),
        ),
    ]
