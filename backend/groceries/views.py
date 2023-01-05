from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Grocery
from .filters import GroceryFilter
from .serializers import GrocerySerializer

class GroceryViewset(viewsets.ModelViewSet):
    serializer_class = GrocerySerializer
    model = Grocery
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = GroceryFilter
    ordering_fields = ("date_added", "name", "bought")
    ordering = ("-date_added")
    queryset = Grocery.objects.all()