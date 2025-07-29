from .models import Account
from .serializers import AccountSerializer, ProfileImageSerializer, RegisterSerializer, UpdateAccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import FileUploadParser

class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer

class UploadProfileImage(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        user = self.get_object(request.user)
        print(request.data['image'])
        serializer = ProfileImageSerializer(user, data=request.data['image'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404

class AccountList(APIView):
    parser_class = (FileUploadParser,)
    """
    List logged in account, or create a new account.
    """
    def get_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        user = request.user
        account = self.get_object(user)
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = self.get_object(request.user)
        print(ProfileImageSerializer(data=request.data))
        serializer = ProfileImageSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        user = self.get_object(request.user)
        serializer = UpdateAccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)