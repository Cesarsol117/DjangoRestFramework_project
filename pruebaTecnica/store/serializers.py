from rest_framework import serializers
from .models import Client, Bill, Product, BillProduct

# se crea cada serializador para la respuesta JSON

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = '__all__'