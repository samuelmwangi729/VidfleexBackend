# Generated by Django 4.1.4 on 2023-01-01 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0009_movie_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-YoR'], 'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
    ]
