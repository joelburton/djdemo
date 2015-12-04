from __future__ import unicode_literals

from django.db import models


class TaskList(models.Model):
    """List of tasks."""

    title = models.CharField(
            max_length=50,
            unique=True,
    )

    def __str__(self):
        return self.title

    def is_complete(self):
        """Are all tasks complete?"""

        # for task in self.task_set.all():
        #     if not task.is_done:
        #         return False
        # return True

        return all(task.is_done for task in self.task_set.all())


class Task(models.Model):
    """A task on a todo list."""

    title = models.CharField(
            max_length=50,
    )
    task_list = models.ForeignKey(
            TaskList,
            null=True,
    )
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    priority = models.CharField(
            max_length=10,
            choices=[('hi', 'High'), ('lo', 'Low')],
    )

    def __str__(self):
        return self.title
