from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CountriesView(APIView):
    """
    List all countries.
    """
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
    
class RegionsView(APIView):
    """
    List all regions.
    """
    def get(self, request, format=None):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

class AreasView(APIView):
    """
    List all areas.
    """
    def get(self, request, format=None):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)