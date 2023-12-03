from django.shortcuts import render
from .models import Vendor, Purchase_order, History
from rest_framework import viewsets
from . serializers import VendorSerializer, Purchase_orderSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class vendor_viewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @swagger_auto_schema(
        operation_summary='Vendor Created',
        operation_description='A new vendor is created successfully',
        # request_body=None,
        responses={201: 'Created', 400: 'Bad Request'},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='List Of vendors',
        operation_description='None',
        responses={200: 'OK'},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        operation_description='Update an item by ID',
        responses={200: 'Updated successfully'},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class purchase_order_viewset(viewsets.ModelViewSet):
    queryset = Purchase_order.objects.all()
    serializer_class = Purchase_orderSerializer

    @swagger_auto_schema(
        operation_summary='Purchase order',
        operation_description='NA',
        # request_body=None,
        responses={201: 'Created', 400: 'Bad Request'},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Get Request',
        operation_description='NA',
        # request_body=None,
        responses={200: 'OK'},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        operation_description='Update an item by ID',
        responses={200: 'Updated successfully'},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


@receiver(post_save, sender=Purchase_order)
def calculate_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        total_completed_pos = Purchase_order.objects.filter(
            vendor=vendor, status='completed').count()
        on_time_completed_pos = Purchase_order.objects.filter(
            vendor=vendor, status='completed', delivery_date__lte=instance.delivery_date).count()
        on_time_delivery_rate = (
            on_time_completed_pos / total_completed_pos) * 100 if total_completed_pos > 0 else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()


class VendorPerformanceView(APIView):

    @swagger_auto_schema(
        operation_summary='Get Request',
        operation_description='NA',
        # request_body=None,
        responses={200: 'OK'},
    )
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)


class AcknowledgePurchaseOrder(APIView):

    @swagger_auto_schema(
        operation_summary='Purchase order',
        operation_description='NA',
        # request_body=None,
        responses={201: 'Created', 400: 'Bad Request'},
    )
    def post(self, request, po_id):
        # Implement your logic to handle PO acknowledgment here
        return Response({"message": "Purchase order acknowledged successfully"})
