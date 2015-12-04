from django.shortcuts import render

# Create your views here.
from django.views import generic

from todo.models import Task, TaskList


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "todo/task_detail.html"


class TaskListListView(generic.ListView):
    model = TaskList


class TaskListDetailView(generic.DetailView):
    model = TaskList

