from django.contrib import admin

from .models import Grocery
from .models import User

admin.site.register(Grocery)
admin.site.register(User)