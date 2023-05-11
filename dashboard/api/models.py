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

COUPON_STATUS = (
    ("RUNNING", "RUNNING"),
    ("FINISHED", "FINISHED")
)

DISCOUNT_TYPE = (
    ("PERCENT", "PERCENT"),
    ("FIXED", "FIXED")
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
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD, default=1, max_length=225)
    delivery_status = models.CharField(choices=DELIVERY_STATUS, default=1, max_length=225)
    amount = models.FloatField(max_length=25)


class CreateCoupons(models.Model):
    title = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=10, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    freeShipping = models.BooleanField(default=False)
    quantity = models.IntegerField()
    discount_type = models.CharField(choices=DISCOUNT_TYPE, default=1, max_length=20)

    def __str__(self):
        return self.title    


class ListCoupons(models.Model):
    coupon = models.OneToOneField(CreateCoupons, on_delete=models.CASCADE, null=True)
    discount = models.FloatField(max_length=10, null=True)
    status = models.CharField(choices=COUPON_STATUS, default=2, max_length=20)

    def __str__(self):
        return self.coupon.title
    

class VendorList(models.Model):
    vendor_name = models.CharField(max_length=225, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    store_name = models.CharField(max_length=225, null=True)
    created_date = models.DateField(auto_now=True)
    revenue = models.FloatField(max_length=10, null=True)

    def __str__(self):
        return self.vendor_name
    

class VendorCreate(models.Model):
    firstname = models.CharField(max_length=225, null=True)
    lastname = models.CharField(max_length=225, null=True)
    email = models.EmailField(max_length=225, null=True)
    password = models.CharField(max_length=225, null=True)
    confirm_password = models.CharField(max_length=225, null=True)

    def __str__(self):
        return {self.firstname, self.lastname}
    

class ProductRelatedPermission(models.Model):
    add_product = models.BooleanField(default=False)
    update_product = models.BooleanField(default=False)
    delete_product = models.BooleanField(default=False)
    apply_discount = models.BooleanField(default=False)


class CategoryRelatedPermission(models.Model):
    add_category = models.BooleanField(default=False)
    update_category = models.BooleanField(default=False)
    delete_category = models.BooleanField(default=False)
    apply_discount = models.BooleanField(default=False)

class Taxes(models.Model):
    tax_detail = models.CharField(max_length=225, null=True)
    tax_rate = models.FloatField(max_length=10, null=True)
    total_tax_amount = models.FloatField(max_length=10, null=True)

    def __str__(self):
        return self.total_tax_amount
    
def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 'INV001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('MAG')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'MAG' + str(formatted)
    return new_invoice_no  

class Invoice(models.Model):
    invoice_no = models.CharField(max_length = 500, default = increment_invoice_number, null = True, blank = True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    shipping_rate = models.FloatField(max_length=10)
    amount_exc_tax = models.FloatField(max_length=225)
    tax = models.FloatField(max_length=10)
    total_amount = models.FloatField(max_length=225, null=True, blank=True)

    def save(self, *args, **kwargs):
        tax_amount = (self.tax / 100) * self.amount_exc_tax
        self.total_amount = self.amount_exc_tax + tax_amount
        super(Invoice, self).save(*args, **kwargs)

