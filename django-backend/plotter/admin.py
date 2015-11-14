from django.contrib import admin

from .models import Measurement

# Register your models here.


class MeasurementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Creation DateTime', {'fields': ['creation_dt']}),
        ('Measurement Value', {'fields': ['value']}),
    ]

admin.site.register(Measurement, MeasurementAdmin)
