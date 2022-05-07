from django.db import models

# Create your models here.


"""
ProductApp  
    -Nom
    -Prix
    -La Quantite en stock
    -Description
    -Image
"""
class productApp(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank= True, null= True)