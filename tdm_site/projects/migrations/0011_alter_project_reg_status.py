# Generated by Django 3.2.12 on 2022-10-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_reg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reg_status',
            field=models.BooleanField(default=False, verbose_name='Registration Status'),
        ),
    ]