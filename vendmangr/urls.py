from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/vendors', views.vendor_viewset.as_view(
        {'get': 'list', 'post': 'create'}), name='vendors'),
    path('api/vendors/<int:pk>', views.vendor_viewset.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='vendor'),

    path('api/purchase_orders', views.purchase_order_viewset.as_view(
        {'get': 'list', 'post': 'create'}), name='purchase_orders'),

    path('api/purchase_orders/<int:pk>', views.purchase_order_viewset.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='purchase_order'),

    path('api/vendors/<int:vendor_id>/performance/',
         views.VendorPerformanceView.as_view(), name='vendor_performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/',
         views.AcknowledgePurchaseOrder.as_view(), name='acknowledge_purchase_order'),
]
