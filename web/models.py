from django.db import models


class Wettkampf(models.Model):
    Ort = models.CharField(max_length=250)
    Datum = models.DateTimeField()
