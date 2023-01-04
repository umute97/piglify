from django.urls import path

from .views import GroceryViewset

urlpatterns = [
    path('', GroceryViewset.as_view({'get': 'list'}), name='groceriesview'),
]