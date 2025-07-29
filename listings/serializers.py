from accounts.serializers import AccountSerializer
from .models import *
from rest_framework import serializers
from misc.serializers import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = "__all__"

class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = "__all__"


class ListingSerializer(serializers.ModelSerializer):
    condition = ConditionSerializer(many=False)
    property_type = PropertyTypeSerializer(many=False)
    category = CategorySerializer(many=False)
    images = ListingImageSerializer(many=True)
    
    country = CountrySerializer(many=False)
    region = RegionSerializer(many=False)
    area = AreaSerializer(many=False)
    agent = AccountSerializer(many=False)

    class Meta:
        model = Listing
        fields = "__all__"

class CreateListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = "__all__"