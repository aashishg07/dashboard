from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import CustomUser

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
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
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


class ListCoupnsView(generics.ListCreateAPIView):
    queryset = ListCoupons.objects.all()
    serializer_class = ListCouponsSerializer

class ListCoupnsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListCoupons.objects.all()
    serializer_class = ListCouponsSerializer


class CreateCouponsListView(generics.ListCreateAPIView):
    queryset = CreateCoupons.objects.all()
    serializer_class = CreateCouponsSerializer

class CreateCouponsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreateCoupons.objects.all()
    serializer_class = CreateCouponsSerializer


class ProductRelatedPermissionListView(generics.ListCreateAPIView):
    queryset = ProductRelatedPermission.objects.all()
    serializer_class = ProductRelatedPermissionSerializer

class ProductRelatedPermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductRelatedPermission.objects.all()
    serializer_class = ProductRelatedPermissionSerializer

class CategoryRelatedPermissionListView(generics.ListCreateAPIView):
    queryset = CategoryRelatedPermission.objects.all()
    serializer_class = CategoryRelatedPermissionSerializer

class CategoryRelatedPermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryRelatedPermission.objects.all()
    serializer_class = CategoryRelatedPermissionSerializer

class TaxesListView(generics.ListCreateAPIView):
    queryset = Taxes.objects.all()
    serializer_class = TaxesSerializer

class TaxesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxes.objects.all()
    serializer_class = TaxesSerializer

class InvoiceListView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer