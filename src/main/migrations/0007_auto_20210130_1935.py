# Generated by Django 3.1.5 on 2021-01-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rainfall_degree_of_strength'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rainfall',
            name='degree_of_strength',
            field=models.CharField(choices=[('Light', 'Light'), ('Medium', 'Medium'), ('Strong', 'Snow')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='rainfall',
            name='type',
            field=models.CharField(choices=[('Rain', 'Rain'), ('Hailstorm', 'Hailstorm'), ('Snow', 'Snow'), ('Fog', 'Fog'), ('Frost', 'Frost')], max_length=30, null=True),
        ),
    ]
