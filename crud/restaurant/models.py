from django.db import models

# Create your models here.

class Item(models.Model):
    itemname = models.TextField(max_length=100)
    amount = models.CharField(max_length=100)
    bought_from= models.CharField(max_length=10)
    bought_on = models.DateField(auto_now=False, auto_now_add=False)
    gst_applied = models.CharField(max_length=15,default="")
    price = models.IntegerField(max_length=15,default="")
    ref = models.FloatField()
    image = models.ImageField(upload_to='',blank=True)
    
    
    


