# Generated by Django 3.2.12 on 2022-03-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=True, max_length=255, verbose_name='Domain')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Slug')),
            ],
        ),
    ]
