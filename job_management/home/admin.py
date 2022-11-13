from django.apps import AppConfig
from django.contrib import admin
from .models import HomePage


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('news','work_schedule', 'week_number')
    list_filter = ('week_number',)
    list_display_links = ('news', 'work_schedule', 'week_number')
    #search_fields = ('news','work_schedule')

admin.site.register(HomePage, HomePageAdmin)