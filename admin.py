from django.contrib import admin

from todo import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin view for tasks."""


@admin.register(models.TaskList)
class TaskListAdmin(admin.ModelAdmin):
    """Admin view for tasks list."""
