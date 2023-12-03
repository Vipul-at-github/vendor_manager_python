from django.contrib import admin
from .models import Vendor, Purchase_order, History
# Register your models here.

admin.site.register(Vendor)

admin.site.register(Purchase_order)

admin.site.register(History)
