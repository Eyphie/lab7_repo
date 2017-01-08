from django.contrib import admin
from django.contrib import admin
from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    def number_of_items(self, request):
        return Item.objects.filter(category_id=request.id).len()
    list_display = ('name', 'number_of_items')
    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Item,ItemAdmin)


