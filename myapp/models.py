from django.db import models
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model for types of items available in the grocery store
class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model for items in the grocery store
class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)  # New field

    def __str__(self):
        return self.name

# Extended Client model inheriting from Django's User model
class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'Waterloo'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')  # Default changed
    interested_in = models.ManyToManyField(Type)
    phone = models.CharField(max_length=15, null=True, blank=True)  # New field

    def __str__(self):
        return self.username

# New model to represent ordered items
class OrderItem(models.Model):
    STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order by {self.client.username} for {self.item.name}"

    def total_price(self):
        return self.quantity * self.item.price

