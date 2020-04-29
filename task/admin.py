from django.contrib import admin

from task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'status', 'created_by', 'updated_at', 'is_deleted',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'status')}
         ),
    )

    list_display = ('title', 'status', 'created_by', 'created_at', 'is_deleted',)
