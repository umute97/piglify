from django.db import models
from django.utils import timezone

USERS = [
    ("umut", "Umut"),
    ("jonny", "Jonny"),
    ("simon", "Simon"),
]

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=50, null=False)
    qty = models.IntegerField(default=1, blank=False, null=False)
    location = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    bought = models.BooleanField(default=False, blank=False, null=False)
    contact = models.CharField(null=True, max_length=10, blank=False, choices=USERS)

    def __str__(self):
        return f"{self.name}: x{self.qty}, bought: {self.bought}"