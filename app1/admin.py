from django.contrib import admin

# Register your models here.
from . models import Product, Category
# from django.contrib.auth.models import User


admin.site.register(Category)
admin.site.register(Product)


# name:mkman
# password:mkman123