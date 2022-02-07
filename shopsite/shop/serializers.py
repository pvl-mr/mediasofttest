from rest_framework import serializers
from .models import *


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"

