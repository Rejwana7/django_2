# Generated by Django 5.0 on 2024-01-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]