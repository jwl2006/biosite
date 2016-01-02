from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PCR_Polymerase(models.Model):
	product_seq = models.CharField(max_length=200)
	product_name = models.CharField(max_length=200)
	product_price = models.DecimalField(max_digits=5, decimal_places=2) 
	product_factory = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date produced')
    

