from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Customer)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

# to update via excel sheet
# @admin.register(Product)
# class ViewAdmin(ImportExportModelAdmin):
#     list_display = ('name','price','category','quantity','digital','desc','image')

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']
admin.site.register(Product,AdminProduct)


class AdminCategory(admin.ModelAdmin):
    list_display = ['name','id']
admin.site.register(Category,AdminCategory)
