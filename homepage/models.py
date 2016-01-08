from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PCR_Polymerase(models.Model):
    seqNo = models.CharField(max_length=200, blank=True, primary_key=True);
    name = models.CharField(max_length=200, blank=True, null=True);
    price = models.DecimalField(max_digits=5, decimal_places=2);
    factory = models.CharField(max_length=200, blank=True, null=True);
    pro_date = models.DateTimeField('date produced');
    unit = models.CharField(max_length=200, blank=True, null=True);
    category = models.CharField(max_length=200, blank=True, null=True);
    lifetime = models.IntegerField(blank=True, null=True);
    def __unicode__(self): 
    	return self.seqNo

