
from django.shortcuts import render
from django.views import View
from .models import Client, Product, Bill, BillProduct
from django.http.response import  JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
import json

# Create your views here.
# realizaremos las vistas basadas en clases

class ClientCreateAPIView(APIView):
    def get(self, request):
        return Response(data = {
    
    "document": 1234567890,
    "first_name": "Default",
    "last_name": "Default",
    "email": "Example@example.com"
                                  })
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientAPIView(APIView):
    def get(self, request):

        client = Client.objects.all()
        client_serializer = ClientSerializer(client, many = True)
        return Response(client_serializer.data, status=status.HTTP_200_OK)

class ClientGetAPIView(APIView):
    def get(self, request, id):

    
        try:
            client = Client.objects.get(id = id)
            client_serializer = ClientSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
    
     
class ClientPutAPIView(APIView):
    def get(self, request, id):
        try:
            client = Client.objects.get(id = id)
            client_serializer = ClientSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id):
        try:
            client = Client.objects.get(id=id)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK, content = "hello" )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDeleteAPIView(APIView):
    
    def get(self, request, id):    
        try:
            client = Client.objects.get(id = id)
            client_serializer = ClientSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        

    def delete(self, request, id):
        try:
            client = Client.objects.get(id=id)       
            client.delete()
            return Response({'message': 'Client deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)