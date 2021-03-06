# Generated by Django 3.1.5 on 2021-01-31 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_task_strength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='rainfall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.rainfall'),
        ),
        migrations.AlterField(
            model_name='task',
            name='strength',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.strength'),
        ),
    ]
