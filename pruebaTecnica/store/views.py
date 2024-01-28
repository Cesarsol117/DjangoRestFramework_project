
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
        
# Bills o facturas
class BillReadAPIView(APIView):
    def get(self, request, *args, **kwargs):
        bills = Bill.objects.all()

        # Serializa todas las facturas y devuelve la respuesta
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# create
class BillCreateAPIView(APIView):
    def get(self, request):
            return Response(data = {
                                    "client": 1,
                                    "company_name": "Default",
                                    "nit": 7894,
                                    "code": 963
                                  })
    
    def post(self, request):
        

        # Supongamos que el cliente_id se pasa como parte de los datos de la solicitud.
        client_id = request.data.get('client', None)

        if client_id is not None:
            # Intenta obtener el cliente con el client_id.
            try:
                client = Client.objects.get(pk=client_id)
            except Client.DoesNotExist:
                return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
            
            # Asigna el cliente a la factura antes de guardarla.
            request.data['client'] = client.id

            serializer = BillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'client_id is required'}, status=status.HTTP_400_BAD_REQUEST)
# Update
class BillUpdateAPIView(APIView):
    def get(self, request, bill_id):    
        try:
            one_bill = Bill.objects.get(id = bill_id)
            bill_serializer = BillSerializer(one_bill)
            return Response(bill_serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, bill_id):
        try:
            # Intenta obtener la factura con el bill_id
            bill = Bill.objects.get(id=bill_id)

            # Actualiza la factura con los nuevos datos
            serializer = BillSerializer(bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Bill.DoesNotExist:
            return Response({'error': 'Bill not found'}, status=status.HTTP_404_NOT_FOUND)
# delete

class BillDeleteAPIView(APIView):
    def get(self, request, bill_id):    
        try:
            one_bill = Bill.objects.get(id = bill_id)
            bill_serializer = BillSerializer(one_bill)
            return Response(bill_serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, bill_id):
        try:
            # Intenta obtener la factura con el bill_id
            bill = Bill.objects.get(id=bill_id)

            # Elimina la factura
            bill.delete()
            return Response({'message': 'Bill deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Bill.DoesNotExist:
            return Response({'error': 'Bill not found'}, status=status.HTTP_404_NOT_FOUND)
# CRUD Productos

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducReadUpdateDeleteAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def get(self, request, product_id):
        product = self.get_object(product_id)
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        if product:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if product:
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
# tabla pivote
class BillProductListCreateAPIView(APIView):
    def get(self, request):
        bill_products = BillProduct.objects.all()
        serializer = BillProductSerializer(bill_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BillProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)