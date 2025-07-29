from .models import *
from .serializers import * # type: ignore
from rest_framework.parsers import FileUploadParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, format=None):
        file_serializer = ListingImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListingsView(APIView):
    """
    List all listings, or create a new listing.
    """
    def get(self, request, format=None):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = Listing.objects.get(pk=serializer.data['id']) # type: ignore
            serializer = ListingSerializer(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingleListingView(APIView):
    """
    Fetch, Edit and Delete listing.
    """
    def get_object(self, pk):
        try:
            return Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        listing = self.get_object(pk)
        serializer = ListingSerializer(listing)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        listing = self.get_object(pk)
        serializer = ListingSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        listing = self.get_object(pk)
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ConditionsView(APIView):
    """
    List all conditions.
    """
    def get(self, request, format=None):
        conditions = Condition.objects.all()
        serializer = ConditionSerializer(conditions, many=True)
        return Response(serializer.data)
    
class CategoriesView(APIView):
    """
    List all categories.
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class PropertyTypesView(APIView):
    """
    List all property types.
    """
    def get(self, request, format=None):
        p_types = PropertyType.objects.all()
        serializer = PropertyTypeSerializer(p_types, many=True)
        return Response(serializer.data)