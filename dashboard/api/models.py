from django.db import models
from django.contrib.auth.models import User


PAYMENT_METHOD = (
    ("PAYMENT1", "PAYMENT1"),
    ("PAYMENT2", "PAYMENT2"),
    ("PAYMENT3", "PAYMENT3"),
    ("PAYMENT4", "PAYMENT4"),
)

DELIVERY_STATUS = (
    ("APPROVED", "APPROVED"),
    ("PENDING", "PENDING"),
    ("REACHED", "REACHED")
)

PAYMENT_STATUS = (
    ("APPROVED", "APPROVED"),
    ("PENDING", "PENDING")
)


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    desc = models.TextField()

    def __str__(self):
        return self.name

class PhysicalProduct(models.Model):
    category = models.CharField(max_length=255, null=True)
    sub_category = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product


class DigitalProduct(models.Model):
    category = models.CharField(max_length=255, null=True)
    sub_category = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product

class ProductReview(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    rating = models.FloatField()
    comment = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name


class OrderList(models.Model):
    image = models.ImageField(upload_to='media/', null=True)
    code = models.CharField(max_length=10, null=True)
    date = models.DateField()
    payment = models.CharField(max_length=20, choices=PAYMENT_METHOD, default='1')
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS, default='1')
    amount = models.FloatField(max_length=225, null=True)

    def __str__(self):
        return self.code
    
class OrderTracking(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    desc = models.TextField()
    location = models.CharField(max_length=225)

    def __str__(self):
        return self.location
    
class OrderDetails(models.Model):
    order_no = models.IntegerField()
    order_items = models.ForeignKey(OrderList, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_no)
    

class Sales(models.Model):
    order_id = models.ForeignKey(OrderList, on_delete=models.CASCADE, null=True)
    product = models.ImageField(upload_to="media/sales/")
    payment_method = models.CharField(choices=PAYMENT_METHOD, default=1, max_length=225)
    payment_status = models.CharField(choices=PAYMENT_STATUS, default=2, max_length=225)
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(max_length=25)

    def __str__(self):
        return self.order_id


class Transactions(models.Model):
    order_id = models.ForeignKey(OrderList, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD, default=1, max_length=225)
    delivery_status = models.CharField(choices=DELIVERY_STATUS, default=1, max_length=225)
    amount = models.FloatField(max_length=25)

