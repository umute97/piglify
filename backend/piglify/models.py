from django.db import models
from django.utils import timezone

class User(models.Model):
    first = models.CharField(max_length=20, null=False)
    last = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"

    @property
    def full_name(self):
        last = "" if self.last is None else self.last
        return f"{self.first} {last}"

class Grocery(models.Model):
    name = models.CharField(max_length=50, null=False)
    qty = models.IntegerField(default=1, blank=False, null=False)
    location = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    bought = models.BooleanField(default=False, blank=False, null=False)
    contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    @property
    def contact_name(self):
        return self.contact.full_name

    def __str__(self):
        return f"{self.name}: x{self.qty}, bought: {self.bought}"
