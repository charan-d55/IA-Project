from django.contrib import admin
# Register your models here.

from django.contrib import admin
from .models import Type, Item, Client, OrderItem

# Register models in the admin interface
admin.site.register(Type)
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(OrderItem)