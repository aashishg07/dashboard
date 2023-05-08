from rest_framework import serializers
from .models import *

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
        fields = ['order_id', 'transaction_id', 'date', 'payment_method', 'delivery_status', 'amount']
