import django_filters

from .models import Grocery

class GroceryFilter(django_filters.FilterSet):
    date_range = django_filters.DateRangeFilter(field_name="date_added")
    start_date = django_filters.DateFilter(field_name="date_added", lookup_expr=("gte"))
    end_date = django_filters.DateFilter(field_name="date_added", lookup_expr=("lte"))

    class Meta:
        model = Grocery
        fields = ["date_added", "id"]

