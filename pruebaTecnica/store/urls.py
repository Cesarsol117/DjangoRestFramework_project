from django.urls import path
from .views import *

# importamos todas las vistas para ponerles una url
# el nombre que va en el navegador, la vista que acompaña, y un endpoint para mostar o llamar.

urlpatterns = [
    path('clients/', ClientView.as_view(), name='ClientList'),
    path('clients/<int:id>', ClientView.as_view(), name='ClientList'),
]
