from django.db import models


# Create your models here.
class Task(models.Model):
    city = models.CharField('City', max_length=30)
    temperature = models.CharField('temperature', max_length=30)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'indicator'
        verbose_name_plural = 'indicators'
