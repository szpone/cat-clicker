from django.db import models

# Create your models here.


class Click(models.Model):
    cats = models.IntegerField
    clicks = models.IntegerField

