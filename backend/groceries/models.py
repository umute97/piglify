from django.db import models
from django.utils import timezone

USERS = [
    ("umut", "Umut"),
    ("jonny", "Jonny"),
    ("simon", "Simon"),
]

class Grocery(models.Model):
    name = models.CharField(max_length=50, null=False)
    qty = models.IntegerField(default=1, blank=False, null=False)
    location = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    bought = models.BooleanField(default=False, blank=False, null=False)
    contact = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return f"{self.name}: x{self.qty}, bought: {self.bought}"

class User(models.Model):
    first = models.CharField(max_length=20, null=False)
    last = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to="profiles/")