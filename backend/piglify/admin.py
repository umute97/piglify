from django.contrib import admin

from .models import Grocery, User, Chore

admin.site.register(Grocery)
admin.site.register(User)
admin.site.register(Chore)