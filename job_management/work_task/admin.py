from django.contrib import admin

from .models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'working_profession', 'phone')
    list_display_links = ('full_name', 'working_profession', 'phone')
    search_fields = ('full_name', 'working_profession')

class Technological_operationAdmin(admin.ModelAdmin):
    list_display = ('name_operations', 'working_profession')
    list_display_links = ('name_operations', 'working_profession')
    search_fields = ('name_operations', 'working_profession')

class Working_professionsAdmin(admin.ModelAdmin):
    list_display = ('profession',)
    list_display_links = ('profession',)
    search_fields = ('profession',)

class Work_taskAdmin(admin.ModelAdmin):
    list_display = ('name_operations', 'full_name', 'time_created',
                    'is_done', 'work_time', 'notes')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Working_professions, Working_professionsAdmin)
admin.site.register(Work_task, Work_taskAdmin)
admin.site.register(Technological_operation, Technological_operationAdmin)
