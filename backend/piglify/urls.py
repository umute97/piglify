from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GroceryViewset
from .views import UserViewset

router = DefaultRouter()
router.register(r'groceries', GroceryViewset, basename="grocery")
router.register(r'users', UserViewset, basename="user")
urlpatterns = [
    path('', include(router.urls))
]