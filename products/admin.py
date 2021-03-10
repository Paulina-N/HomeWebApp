from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 30

admin.site.register(Product, ProductAdmin)