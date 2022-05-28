from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('group',)


admin.site.register(Task, TaskAdmin)