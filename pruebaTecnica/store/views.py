from django.shortcuts import render
from django.views import View
from .models import Client, Product, Bill, BillProduct
from django.http.response import JsonResponse

# Create your views here.
# realizaremos las vistas basadas en clases

class ClientView(View):
    def get(self, request):
        client_list = list(Client.objects.values())
        if len(client_list) > 0:
            data_client = {'message':'Exito',
                       'name_client': client_list
                       }
        else:
            data_client = {'message':'No encontrado'}
        return JsonResponse(data_client)