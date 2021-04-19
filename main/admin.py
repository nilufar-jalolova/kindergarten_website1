from django.contrib import admin

from main.models import StaffModel, GalleryModel, NewsModel, BannerModel, ContactModel


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'info', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'info']


@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'image', 'created_at']
    search_fields = ['image', 'created_at']
    list_filter = ['created_at']


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'content', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['title', 'created_at']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['image', 'created_at']
    search_fields = ['created_at']
    list_filter = ['image', 'created_at']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'text', 'created_at']
    search_fields = ['name', 'phone']
    list_filter = ['name', 'phone']
