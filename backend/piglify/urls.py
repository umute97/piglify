from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ChoreViewset, GroceryViewset, UserViewset

router = DefaultRouter()
router.register(r'groceries', GroceryViewset, basename="grocery")
router.register(r'users', UserViewset, basename="user")
router.register(r'chores', ChoreViewset, basename="chore")
urlpatterns = [
    path('', include(router.urls))
]