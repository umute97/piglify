from rest_framework import serializers

from .models import Grocery

class GrocerySerializer(serializers.ModelSerializer):
    date_added = serializers.ReadOnlyField()

    class Meta:
        model = Grocery
        fields = '__all__'