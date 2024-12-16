from rest_framework import serializers
from .models import Buyer, Game
from django.contrib.auth.models import User

class BuyerSerializer(serializers.ModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Buyer
        fields = '__all__'

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Возраст не может быть отрицательным")
        return value

class GameSerializer(serializers.ModelSerializer):
    buyers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'

    def validate_cost(self, value):
        if value < 0:
            raise serializers.ValidationError("Стоимость не может быть отрицательной")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']