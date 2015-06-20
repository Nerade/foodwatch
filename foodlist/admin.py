from django.contrib import admin
from foodlist.models import Category, Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    fields= '__all__'
    read_only=['premium_cost','member_cost','guest_cost',]

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item)
admin.site.register(Category)