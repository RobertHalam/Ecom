from django.contrib import admin

from .models.customer import Customer
from .models.product import Product
from .models.category import Category



class AdminProduct(admin.ModelAdmin):
    list_display = ['prod_name','prod_price','prod_category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['cate_name',]


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)