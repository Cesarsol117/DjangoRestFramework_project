from django.urls import path
from .views import *

# importamos todas las vistas para ponerles una url
# el nombre que va en el navegador, la vista que acompaña, y un endpoint para mostar o llamar.

urlpatterns = [
    path('new-client/', ClientCreateAPIView.as_view(), name='new_clients'),
    path('clients/', ClientAPIView.as_view(), name='all_clients'),
    path('detail-client/<int:id>', ClientGetAPIView.as_view(), name='one_clients'),
    path('clients/<int:id>/', ClientPutAPIView.as_view(), name='client-put'),
    path('delete-clients/<int:id>/', ClientDeleteAPIView.as_view(), name='client-Delete'),
#    urls de Bilss
    path('all-bills/', BillReadAPIView.as_view(), name='all_bills'),
    path('new-bills/', BillCreateAPIView.as_view(), name='new_bills'),
    path('update-bills/<int:bill_id>/', BillUpdateAPIView.as_view(), name='update_bills'),
    path('delete-bills/<int:bill_id>/', BillDeleteAPIView.as_view(), name='delete_bills'),
    # urls de products
    path('products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    path('products/<int:product_id>/', ProducReadUpdateDeleteAPIView.as_view(), name='product_retrieve_update_destroy'),
    # tabla pivote
    path('billproducts/', BillProductListCreateAPIView.as_view(), name='billproduct-list-create'),
]
