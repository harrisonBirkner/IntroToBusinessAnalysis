from django.contrib import admin
from .models import Customer,Order,Basket,Orders_Num
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(Orders_Num)

