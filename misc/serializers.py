from .models import *
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False)
    class Meta:
        model = Region
        fields = "__all__"

class AreaSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=False)

    class Meta:
        model = Area
        fields = "__all__"