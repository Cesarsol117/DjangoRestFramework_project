from typing import Any
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .models import Client, Product, Bill, BillProduct
from django.http.response import HttpResponse as HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APiView
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
import json

# Create your views here.
# realizaremos las vistas basadas en clases

class ClientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id = 0):
        if (id>0):
            client_list = list(Client.objects.filter(id=id).values())
            if len(client_list)>0:
                one_client = client_list[0]
                data_client = {'message':'Success',
                               'client': one_client
                               }
            else:
                data_client={'message':'Not found'}
            return JsonResponse(data_client)
        else:
            
            client_list = list(Client.objects.values())
            if len(client_list) > 0:
                data_client = {'message':'Exito',
                        'client': client_list
                        }
            else:
                data_client = {'message':'No encontrado'}
            return JsonResponse(data_client)
    
    def post(self, request):
        json_body = json.loads(request.body)
        Client.objects.create(document = json_body['document'], first_name = json_body['first_name'], last_name = json_body['last_name'], email = json_body['email'], )
        data_client = {'message':'Exito'}
        return JsonResponse(data_client)
    
    def put(self, request, id):
        json_body = json.loads(request.body)
        client_list = list(Client.objects.filter(id=id).values())
        if len(client_list)>0:
            one_client = Client.objects.get(id=id)
            one_client.document = json_body['document']
            one_client.first_name = json_body['first_name']
            one_client.last_name = json_body['last_name']
            one_client.email = json_body['email']
            one_client.save()
            data_client = {'message':'Success'}
            
        else:
            data_client = {'message':'Not Found'}
        return JsonResponse(data_client)