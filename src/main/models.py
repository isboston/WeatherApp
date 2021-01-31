from django.db import models


# Create your models here.
class Rainfall(models.Model):
    type_rainfall = [
        ('Rain', 'Rain'),
        ('Hailstorm', 'Hailstorm'),
        ('Snow', 'Snow'),
        ('Fog', 'Fog'),
        ('Frost', 'Frost'),
    ]
    degree_of_strength = [
        ('Light', 'Light'),
        ('Medium', 'Medium'),
        ('Strong', 'Strong'),
    ]
    type = models.CharField(max_length=30, null=True, choices=type_rainfall)
    degree_of_strength = models.CharField(max_length=30, null=True, choices=degree_of_strength)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'rainfall'
        verbose_name_plural = 'rainfalls'
        ordering = ['-type']


class Location(models.Model):
    CHOICES = [
        ('Belarus', (
            ('Minsk Region', 'Minsk Region'),
            ('Gomel Region', 'Gomel Region'),
            ('Brest Region', 'Brest Region'),
            ('Grodno Region', 'Grodno Region'),
            ('Vitebsk Region', 'Vitebsk Region'),
            ('Mogilev Region', 'Mogilev Region'),
        )
         ),
        ('Ukraine', (
            ('Kyiv', 'Kyiv'),
            ('Chernihiv', 'Chernihiv'),
        )
         ),
    ]
    region = models.CharField(max_length=300, choices=CHOICES)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'


class Task(models.Model):
    city = models.CharField('City', max_length=30)
    temperature = models.CharField('temperature', max_length=30)
    date_pub = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.PROTECT, verbose_name='location')
    rainfall = models.ForeignKey(Rainfall, null=True, on_delete=models.PROTECT, verbose_name='rainfall')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'weather'
        verbose_name_plural = 'weathers'
        ordering = ['-city']
