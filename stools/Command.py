# -*- coding: utf-8 -*-

"""
    Module for command management
"""

from stools.Colors import Colors

class Command(object):
    """
       Representation of a command
    """

    def __init__(self, name, machine, command_line):
        """
            Create a new Command object

            :param name: command name
            :param machine: object Machine where execute command
            :param command_line: string of command line
            :return: Command instance
            :rtype: Command
        """
        self.name = name
        self.machine = machine
        self.command_line = command_line

    def execute(self):
        """
            Execute this command 

            :return: return of the command
            :rtype: string
        """
        prompt = "[" + self.machine.username + "@" + self.machine.ip + "]"
        command_line = self.command_line
        print Colors.enable_color("red") + prompt + " " + command_line + Colors.disable_color()
        return self.machine.execute_command(self.command_line)

