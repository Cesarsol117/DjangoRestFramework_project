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
]
