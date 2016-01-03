# -*- coding: utf-8 -*-

"""
    Module for tasks management
"""

class Task(object):
    """
        Representation of a task
    """

    def __init__(self, name):
        """
            Create a new Task object

            :param name: task name
            :return: Task instance
            :rtype: Task
        """
        self.name = name
        self.commands_list = []

    def add_command(self, command):
        """
            Add command to this task commands list

            :param command: command to add to commands list
        """
        self.commands_list.append(command)

    def execute(self):
        """
            Execute all commands that components this task
        """
        for command in self.commands_list:
            stdout = command.execute()
            print stdout + '\n'

