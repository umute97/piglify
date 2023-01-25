from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend

from .models import Grocery, User
from .filters import GroceryFilter
from .serializers import GrocerySerializer, UserSerializer

class GroceryViewset(viewsets.ModelViewSet):
    serializer_class = GrocerySerializer
    model = Grocery
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = GroceryFilter
    ordering_fields = ("date_added", "name", "bought")
    ordering = ("-date_added")
    queryset = Grocery.objects.all()

    @action(detail=True, methods=['post'])
    def update_bought(self, request, pk=None):
        grocery = self.get_object()
        status = bool(request.data.get("bought", None))
        grocery.bought = status
        grocery.save()
        return Response({'bought': status})
    
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

