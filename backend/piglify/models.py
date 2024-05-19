import datetime
from django.db import models
from django.utils import timezone

CHORES = [
    ("kitchen", "Kitchen"),
    ("bath", "Bath + Restroom"),
    ("vacuum", "Wipe and Vacuum")
]
class Chore(models.Model):
    name = models.CharField(choices=CHORES, max_length=30, null=False, blank=False)
    desc = models.CharField(max_length=2000, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    first = models.CharField(max_length=20, null=False)
    last = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to="profiles/", null=True, blank=True)
    initial_chore = models.ForeignKey(Chore, on_delete=models.CASCADE, null=True, blank=True)
    done = models.BooleanField(default=False, null=False, blank=False)
    done_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"

    @property
    def full_name(self):
        last = "" if self.last is None else self.last
        return f"{self.first} {last}"
    
    @property
    def chore(self):
        today = datetime.date.today()
        start_date = self.initial_chore.date_added.date()
        start_wed = start_date - datetime.timedelta(days=start_date.weekday()-2)  # Set the start date to the most recent Wednesday
        week_number = (today - start_wed).days // 7
        _id = (self.initial_chore.id + week_number) % 3 + 1
        return [Chore.objects.get(pk=_id)]
    
    @property
    def next_chore(self):
        today = datetime.date.today()
        start_date = self.initial_chore.date_added.date()
        start_wed = start_date - datetime.timedelta(days=start_date.weekday()-2)  # Set the start date to the most recent Wednesday
        week_number = (today - start_wed).days // 7
        _id = (self.initial_chore.id + 1 + week_number) % 3 + 1
        return [Chore.objects.get(pk=_id)]

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
