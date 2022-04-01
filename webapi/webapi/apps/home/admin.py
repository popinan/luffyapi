from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'orders', 'is_show', 'is_delete']
