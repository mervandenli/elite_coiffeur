from django.contrib import admin
from . import models

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(models.Feedback, FeedbackAdmin)