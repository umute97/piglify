import django_filters

from .models import Grocery

class GroceryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    contact = django_filters.CharFilter(field_name="contact", lookup_expr="icontains")
    location = django_filters.CharFilter(field_name="location", lookup_expr="icontains")
    bought = django_filters.BooleanFilter(field_name="bought")

    class Meta:
        model = Grocery
        fields = ["name", "contact", "location", "bought"]

