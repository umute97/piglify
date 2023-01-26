import datetime
from django.db import models
from django.utils import timezone

CHORES = [
    ("kitchen", "Kitchen"),
    ("bath", "WC + Bath"),
    ("vacuum", "Wipe and Vacuum")
]
class Chore(models.Model):
    name = models.CharField(choices=CHORES, max_length=30, null=False, blank=False)
    desc = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    first = models.CharField(max_length=20, null=False)
    last = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to="profiles/", null=True, blank=True)
    initial_chore = models.ForeignKey(Chore, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"

    @property
    def full_name(self):
        last = "" if self.last is None else self.last
        return f"{self.first} {last}"
    
    @property
    def chore(self):
        now = datetime.datetime.utcnow().replace(tzinfo=timezone.utc)
        m1 = (now - datetime.timedelta(days=now.weekday()))
        m2 = (self.initial_chore.date_added - datetime.timedelta(days=self.initial_chore.date_added.weekday()))
        return (m1 - m2).days % 3 + self.initial_chore.id

class Grocery(models.Model):
    name = models.CharField(max_length=50, null=False)
    qty = models.IntegerField(default=1, blank=False, null=False)
    location = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    bought = models.BooleanField(default=False, blank=False, null=False)
    contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    @property
    def contact_name(self):
        return self.contact.full_name

    def __str__(self):
        return f"{self.name}: x{self.qty}, bought: {self.bought}"
