from django.urls import path

from .views import GroceryViewset
from .views import UserViewset

urlpatterns = [
    path('groceries', GroceryViewset.as_view({'get': 'list'}), name='groceriesview'),
    path('users', UserViewset.as_view({'get': 'list'}), name='usersview'),
]