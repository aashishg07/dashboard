from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'desc']

    
class PhysicalProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = PhysicalProduct
        fields = ['id', 'category', 'sub_category', 'product']


class DigitalProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = DigitalProduct
        fields = ['id', 'category', 'sub_category', 'product']


class ProductReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.StringRelatedField()
    product_name = serializers.StringRelatedField()
    class Meta:
        model = ProductReview
        fields = ['id', 'customer_name', 'product_name', 'rating', 'comment', 'published']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = ['id', 'image', 'code', 'date', 'payment', 'delivery_status', 'amount']

class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = ['id', 'date', 'time', 'desc', 'location']

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderListSerializer(many=True)
    class Meta:
        model = OrderDetails
        fields = ['id', 'order_no', 'order_items']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['id', 'order_id', 'product', 'payment_method', 'payment_status', 'date', 'total']

    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['id', 'order_id', 'date', 'payment_method', 'delivery_status', 'amount']


class CreateCouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateCoupons
        fields = ['id', 'title', 'code', 'start_date', 'end_date', 'freeShipping', 'quantity', 'discount_type']



class ListCouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListCoupons
        fields = ['id', 'coupon', 'discount', 'status']



class ProductRelatedPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRelatedPermission
        fields = ['id', 'add_product', 'update_product', 'delete_product', 'apply_discount']


class CategoryRelatedPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRelatedPermission
        fields = ['id', 'add_category', 'update_category', 'delete_category', 'apply_discount']

class TaxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxes
        fields = ['id', 'tax_detail', 'tax_rate', 'total_tax_amount']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_no', 'date', 'time', 'shipping_rate', 'amount_exc_tax', 'tax', 'total_amount']