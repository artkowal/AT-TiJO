import unittest
from lab03_TDD.src.task_list import TaskList

# RED       1 KROK (*)
# GREEN     2 KROK (*)
# REFACTOR  3 KROK (*)
# ...
# RED...

class TaskListTestCase(unittest.TestCase):
    def test_add_task_should_add_task_to_list(self):
        # given
        task_list = TaskList()

        # when
        task_list.add_task("Buy milk")

        # then
        self.assertEqual(task_list.tasks(), ["Buy milk"])


    def test_add_multiple_tasks_should_add_all_tasks_to_list(self):
        # given
        task_list = TaskList()

        # when
        task_list.add_task("Buy milk")
        task_list.add_task("But cornflakes")

        # then
        self.assertEqual(task_list.tasks(), ["Buy milk", "But cornflakes"])


    def test_remove_task_should_remove_task_from_list(self):
        # given
        task_list = TaskList()
        task_list.add_task("Buy milk")
        task_list.add_task("Buy cornflakes")

        # when
        task_list.remove_task("Buy milk")

        # then

        self.assertEqual(task_list.tasks(), ["Buy cornflakes"])


    def test_remove_task_should_do_nothing_if_task_not_in_list(self):
        # given
        task_list = TaskList()
        task_list.add_task("Buy milk")

        # when
        task_list.remove_task("Buy cornflakes")

        # then
        self.assertEqual(task_list.tasks(), ["Buy milk"])


if __name__ == '__main__':
    unittest.main()