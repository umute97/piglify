from rest_framework import serializers

from .models import Chore, Grocery
from .models import User

class ChoreSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Chore
        fields = '__all__'
    
    def get_name(self, obj):
        return obj.get_name_display()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    chore = ChoreSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

class GrocerySerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(read_only=True, format=r'%d.%m.%Y, %H:%M')
    contact_name = serializers.ReadOnlyField()

    class Meta:
        model = Grocery
        fields = '__all__'
