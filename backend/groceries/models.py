from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=50, null=False)
    qty = models.IntegerField(default=1, blank=False, null=False)
    location = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    bought = models.BooleanField(default=False, blank=False, null=False)