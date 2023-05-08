from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductListViews.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailViews.as_view(), name='product_detail'),
    path('physical-products/', PhysicalProductListViews.as_view(), name='physical_product_list'),
    path('physical-products/<int:pk>/', PhysicalProductDetailViews.as_view(), name='physical_product_detail'),
    path('digital-products/', DigitalProductListViews.as_view(), name='digital_product_list'),
    path('digital-products/<int:pk>/', DigitalProductDetailViews.as_view(), name='digital_product_detail'),
    path('products/review/', ProductReviewListView.as_view(), name='review_product_list'),
    path('products/review/<int:pk>/', ProductReviewDetailView.as_view(), name='review_product_detail'),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
    path('order-list/<int:pk>/', OrderListDetailView.as_view(), name='orderlist_detail'),
    path('order-tracking/', OrderTrackingListView.as_view(), name='order_tracking_list'),
    path('order-tracking/<int:pk>/', OrderTrackingDetailView.as_view(), name='order_tracking_detail'),
    path('order-details/', OrderDetailsListView.as_view(), name='order_detail_list'),
    path('order-details/<int:pk>/', OrderDetailsView.as_view(), name='order_detail'),
    path('sales/', SalesListView.as_view(), name='sales_list'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='sales_detail'),
    path('transactions/', TransactionListView.as_view(), name='transactions_list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transactions_detail'),
]
