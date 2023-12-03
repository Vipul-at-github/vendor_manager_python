from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    vendor_code = models.CharField(primary_key=True, max_length=200)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.DurationField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name


class Purchase_order(models.Model):
    po_number = models.CharField(max_length=200, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    delivery_date = models.DateTimeField('date delivered')
    items = JSONField
    quantity = models.IntegerField()
    status = models.CharField(max_length=200)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField('date issued')
    acknowledgement_date = models.DateTimeField('date acknowledged', null=True)


class History(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField('date')
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
