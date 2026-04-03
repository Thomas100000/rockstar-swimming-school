from django.contrib import admin
from .models import Enquiry, Coach, GalleryImage

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_number', 'created_at')
    search_fields = ('name', 'email', 'mobile_number')

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
