# Generated by Django 3.1.5 on 2021-01-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210130_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rainfall',
            options={'ordering': ['-type'], 'verbose_name': 'rainfall', 'verbose_name_plural': 'rainfalls'},
        ),
        migrations.RemoveField(
            model_name='rainfall',
            name='name',
        ),
        migrations.AddField(
            model_name='rainfall',
            name='type',
            field=models.CharField(choices=[('Rainfall', (('Rain', 'Rain'), ('Hailstorm', 'Hailstorm'), ('Snow', 'Snow'), ('Fog', 'Fog'), ('Frost', 'Frost')))], max_length=30, null=True),
        ),
    ]
