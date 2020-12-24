from django.contrib import admin

from .models import Product
from .models import Client
from .models import Employee


admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Employee)

