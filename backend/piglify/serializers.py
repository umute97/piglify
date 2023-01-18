from rest_framework import serializers

from .models import Grocery
from .models import User


class GrocerySerializer(serializers.ModelSerializer):
    date_added = serializers.ReadOnlyField()
    contact = serializers.CharField(
        source='contact.full_name',
        read_only=True
    )

    class Meta:
        model = Grocery
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = '__all__'
