from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

class ProductListViews(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PhysicalProductListViews(generics.ListCreateAPIView):
    queryset = PhysicalProduct.objects.all()
    serializer_class = PhysicalProductSerializer


class PhysicalProductDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhysicalProduct.objects.all()
    serializer_class = PhysicalProductSerializer


class DigitalProductListViews(generics.ListCreateAPIView):
    queryset = DigitalProduct.objects.all()
    serializer_class = DigitalProductSerializer


class DigitalProductDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = DigitalProduct.objects.all()
    serializer_class = DigitalProductSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductReviewListView(generics.ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


class OrderListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


class OrderTrackingListView(generics.ListCreateAPIView):
    queryset = OrderTracking.objects.all()
    serializer_class = OrderTrackingSerializer


class OrderTrackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderTracking.objects.all()
    serializer_class = OrderTrackingSerializer


class OrderDetailsListView(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer


class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer

class SalesListView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class TransactionListView(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer