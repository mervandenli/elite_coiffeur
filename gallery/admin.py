from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name','image','created_date')
    list_display_links = ('name','image','created_date')
    list_filter = ('created_date',)
    search_fields = ('name','image','created_date')
    list_per_page = 10

admin.site.register(Photo,PhotoAdmin)