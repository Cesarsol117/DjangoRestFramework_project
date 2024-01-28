from django.db import models

# Create your models here.

# creo modelos los cuales son las tablas.
class Client(models.Model):
    document = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.PositiveIntegerField(unique=True)
    code = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"Bill-{self.id} for {self.client.first_name} {self.client.last_name}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
# mi tabla pivote para unir las tablas bill y products
class BillProduct(models.Model):
    id = models.AutoField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bill-{self.bill.id} Product-{self.product.id}"