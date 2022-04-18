from django.contrib import admin
from .models import Banner, Nav


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'orders', 'is_show', 'is_delete']


@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'position', 'is_show', 'is_site']