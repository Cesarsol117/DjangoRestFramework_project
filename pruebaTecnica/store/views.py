
from django.shortcuts import render
from django.views import View
from .models import Client, Product, Bill, BillProduct
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
import json

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import UserRegistrationSerializer

import csv
from django.http import HttpResponse

from rest_framework.parsers import FileUploadParser

from django.shortcuts import render
# Create your views here.
# realizaremos las vistas basadas en clases

class ClientCreateAPIView(APIView):
        
    permission_classes = [IsAuthenticated]
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

class ClientAPIView(LoginRequiredMixin, APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):

        client = Client.objects.all()
        client_serializer = ClientSerializer(client, many = True)
        return Response(client_serializer.data, status=status.HTTP_200_OK)

class ClientGetAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):

    
        try:
            client = Client.objects.get(id = id)
            client_serializer = ClientSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
    
     
class ClientPutAPIView(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    def get(self, request):
        bills = Bill.objects.all()

        # Serializa todas las facturas y devuelve la respuesta
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# create
class BillCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
class BillProductReadUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, bill_id, product_id):
        try:
            return BillProduct.objects.get(bill_id=bill_id, product_id=product_id)
        except BillProduct.DoesNotExist:
            return None

    def get(self, request, bill_id, product_id):
        bill_product = self.get_object(bill_id, product_id)
        if bill_product:
            serializer = BillProductSerializer(bill_product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'BillProduct not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, bill_id, product_id):
        bill_product = self.get_object(bill_id, product_id)
        if bill_product:
            serializer = BillProductSerializer(bill_product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'BillProduct not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, bill_id, product_id):
        bill_product = self.get_object(bill_id, product_id)
        if bill_product:
            bill_product.delete()
            return Response({'message': 'BillProduct deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'BillProduct not found'}, status=status.HTTP_404_NOT_FOUND)
# Registro de usuario
class UserRegistrationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(data = {
                                    "username": "default",
                                    "email": "default",
                                    "password": "default",
                                    "first_name": "default",
                                    "last_name": "default"
                                  })
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# download los registros del cliente a csv
class ClientCSVDownloadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener la lista de clientes con información requerida
        clients = Client.objects.all()
        # unalista vacia para colocar los datos
        data = []

        for client in clients:
            client_data = {
                'documento': client.document,
                'nombre_completo': f"{client.first_name} {client.last_name}",
                'cantidad_facturas': client.bill_set.count()  # Obtener la cantidad de facturas relacionadas
            }
            data.append(client_data)

        # Crear el archivo CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

        # Escribir los datos en el archivo CSV
        writer = csv.writer(response)
        writer.writerow(['Documento', 'Nombre Completo', 'Cantidad de Facturas'])
        # un for para cada registro se guarde en la lista data
        for client_data in data:
            writer.writerow([client_data['documento'], client_data['nombre_completo'], client_data['cantidad_facturas']])

        return response
    
# cargar los archivos de csv para la creacion de clientes

class ClientCSVUploadAPIView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'No hay un archivo CSV'}, status=status.HTTP_400_BAD_REQUEST)

        # Procesar el archivo CSV 
        clients_data = []
        try:
            decoded_file = file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)
            
            for row in csv_reader:
                clients_data.append({
                    'document': row.get('Documento'),
                    'first_name': row.get('Nombre'),
                    'last_name': row.get('Apellido'),
                    'email': row.get('Correo')
                    # Añade más campos según sea necesario
                })
        except csv.Error as e:
            return Response({'error': f'Error al procesar el archivo CSV: {e}'}, status=status.HTTP_400_BAD_REQUEST)

        # Crear clientes a partir de los datos del CSV
        created_clients = []
        for data in clients_data:
            serializer = ClientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                created_clients.append(serializer.data)

        return Response({'message': 'Carga de CSV exitosa', 'created_clients': created_clients}, status=status.HTTP_201_CREATED)
# Para las consultas usasndo el ORM

def all_products(request):
    all_products = Product.objects.all()
    product_data = [{'name': product.name, 'description': product.description} for product in all_products]
    return JsonResponse({'products': product_data})

def llaves_bristol(request):
    bristol_keys = Product.objects.filter(name__icontains='llave')
    bristol_data = [{'name': key_bristol.name, 'description': key_bristol.description} for key_bristol in bristol_keys]
    return JsonResponse({'bristol_keys': bristol_data})
