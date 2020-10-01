from django.contrib import admin

# Register your models here.
from lesTaches.models import Task
from lesTaches.models import User


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date', 'colored_due_date')

admin.site.register(Task, TaskAdmin)
admin.site.register(User)