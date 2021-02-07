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
    type = models.CharField(max_length=30, null=True, choices=type_rainfall)
    strength = models.ForeignKey('Strength', null=True, on_delete=models.PROTECT, verbose_name='strength')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'rainfall'
        verbose_name_plural = 'rainfalls'
        ordering = ['-type']


class Strength(models.Model):
    degree_of_strength = [
        ('Light', 'Light'),
        ('Medium', 'Medium'),
        ('Strong', 'Strong'),
    ]
    degree = models.CharField(max_length=30, null=True, choices=degree_of_strength)

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'strength'
        verbose_name_plural = 'strengths'
        ordering = ['-degree']


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
    rainfall = models.ForeignKey(Rainfall, null=True, on_delete=models.PROTECT, blank=True)
    strength = models.ForeignKey(Strength, null=True, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'weather'
        verbose_name_plural = 'weathers'
        ordering = ['-id']


class City(models.Model):
    name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'
        ordering = ['-id']
