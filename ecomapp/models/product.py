from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category

class Product(models.Model):
    prod_name = models.CharField(max_length= 50)
    prod_price = models.IntegerField(default=0)
    prod_category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    prod_description = models.CharField(max_length=200,default="",null=True,blank=True)
    prod_image = models.ImageField(upload_to='uploads/products/')




    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    
    
    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(prod_category = category_id)

        else:
            return Product.get_all_product()