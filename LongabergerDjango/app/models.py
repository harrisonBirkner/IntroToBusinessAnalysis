from django.db import models

# Create your models here.

class Customer(models.Model):
	 customer_id = models.AutoField(primary_key = True)
	 first_name = models.CharField(max_length = 25)
	 last_name = models.CharField(max_length = 25)
	 address = models.CharField(max_length = 50)
	 state = models.CharField(max_length = 2)
	 zip_code = models.CharField(max_length = 5)
	 phone_num = models.CharField(max_length = 12)
	 email = models.EmailField()

class Order(models.Model):
	order_num = models.AutoField(primary_key = True)
	customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
	order_date = models.DateField()
	ship_date = models.DateField()
	total = models.DecimalField(max_digits = 10, decimal_places=2)

class Basket(models.Model):
	basket_id = models.AutoField(primary_key = True)
	description = models.CharField(max_length = 100)
	cost = models.DecimalField(max_digits=5,decimal_places=2)

class Orders_Num (models.Model):
	order_num = models.ForeignKey(Order,on_delete=models.CASCADE)
	basket_id = models.ForeignKey(Basket,on_delete = models.CASCADE)
