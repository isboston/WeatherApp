from django.contrib import admin
from .models import Task, Location, Rainfall, Strength

admin.site.register(Task)
admin.site.register(Location)
admin.site.register(Rainfall)
admin.site.register(Strength)