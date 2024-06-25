from django.db import models
# Create your models here.

class plat(models.Model):
   name  = models.CharField(max_length=200)
   priceM = models.DecimalField(max_digits=4, decimal_places=3)
   priceL = models.DecimalField(max_digits=4, decimal_places=3)
   pImage = models.URLField()


class boisson(models.Model):
   name  = models.CharField(max_length=200)
   priceM = models.DecimalField(max_digits=4, decimal_places=3)
   priceL = models.DecimalField(max_digits=4, decimal_places=3)
   bImage = models.URLField()

