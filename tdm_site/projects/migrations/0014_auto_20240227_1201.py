# Generated by Django 3.2.12 on 2024-02-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_project_deafpods_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='indy_bool',
            field=models.BooleanField(default=False, verbose_name='INDY'),
        ),
        migrations.AddField(
            model_name='project',
            name='ndmn_bool',
            field=models.BooleanField(default=False, verbose_name='NDMN'),
        ),
        migrations.AddField(
            model_name='project',
            name='wl_bool',
            field=models.BooleanField(default=False, verbose_name='WL'),
        ),
    ]
