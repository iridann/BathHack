from django.db import models

# Create your models here.


class Measurement(models.Model):
    creation_dt = models.DateTimeField('Creation DateTime')
    value = models.FloatField()

    def __str__(self):
        return "value: {} created: {}".format(self.value, self.creation_dt)
