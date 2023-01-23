from rest_framework import serializers

from .models import Grocery
from .models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = '__all__'

class GrocerySerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(read_only=True, format=r'%d.%m.%Y, %H:%M')
    contact_name = serializers.ReadOnlyField()

    class Meta:
        model = Grocery
        fields = '__all__'
