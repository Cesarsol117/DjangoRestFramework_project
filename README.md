# DjangoRestFramework_project
Repositorio de Django Rest Framework

Despliegue de la Aplicación Django con Clientes, CSV y Autenticación JWT

Esta aplicación Django proporciona endpoints para gestionar clientes, cargar archivos CSV y autenticación JWT. Sigue los pasos a continuación para desplegar la aplicación.

## Requisitos Previos

- Python >= 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt


## Pasos de Despliegue

1. **Clona el Repositorio**
`$ python -m venv venv`

2. **Clona el Repositorio**
`$ venv\Scripts\activate`


3. **Clona el Repositorio**

   <https://github.com/Cesarsol117/DjangoRestFramework_project.git>
   
4. **instala dependencias**
`$ pip install -r requirements.txt`

5. **Configura tu base de datos**
`$ python manage.py migrate`

6. **Crea superusuario**
`$ python manage.py createsuperuser`

7. **inicia el servidor de desarrollo**
`$ python manage.py runserver`
La aplicación estará disponible en http://localhost:8000/.

8. **Accede a la Interfaz de Administración (Opcional)**

    Accede a http://localhost:8000/admin/ con las credenciales del superusuario para administrar los datos.
9. **Prueba los Endpoints de la API**

    Puedes utilizar herramientas como Postman o curl para probar los endpoints de la API.
10. **Carga un Archivo CSV**

    Utiliza el endpoint /upload-client-csv/ para cargar un archivo CSV con registros de clientes.
11. **Genera un Token JWT**
    Utiliza el endpoint store/token/ para obtener un token JWT con las credenciales de un usuario.

12. **Protege tus Endpoints con JWT**
    Incluye el token JWT obtenido en la cabecera de tus solicitudes para proteger los endpoints que requieren autenticación.

## Contribuciones
    Si encuentras errores o mejoras posibles, por favor, contribuye a través de issues o pull requests.

## Licencia

    Este proyecto está bajo la licencia MIT.

Este README proporciona una guía básica para clonar el repositorio, instalar dependencias, configurar la base de datos, iniciar el servidor de desarrollo y probar la aplicación. Asegúrate de personalizar la información según las características específicas de tu proyecto. Además, si tienes instrucciones específicas para el despliegue en un entorno de producción, puedes incluirlas en la sección correspondiente.

