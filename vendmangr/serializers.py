from rest_framework import serializers
from . import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = '__all__'


class Purchase_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase_order
        fields = '__all__'
