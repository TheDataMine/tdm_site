# Generated by Django 3.2.12 on 2024-02-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20240227_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.IntegerField(default=2024, verbose_name='year'),
        ),
    ]
