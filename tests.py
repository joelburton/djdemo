from django.test import TestCase

from todo.models import TaskList, Task


class TaskTestCase(TestCase):
    def test_is_complete(self):
        tl = TaskList.objects.create(title='Stuff To Do')
        t = Task.objects.create(title='Go running',
                                description='Yes!',
                                task_list=tl,
                                is_done=True)

        self.assertTrue(tl.is_complete())
