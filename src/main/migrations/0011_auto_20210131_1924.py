# Generated by Django 3.1.5 on 2021-01-31 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210131_1100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-id'], 'verbose_name': 'weather', 'verbose_name_plural': 'weathers'},
        ),
    ]
