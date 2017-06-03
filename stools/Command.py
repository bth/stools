# -*- coding: utf-8 -*-

"""
    Module for command management
"""

class Command(object):
    """
       Representation of a command
    """

    def __init__(self, name, machine, command_line, timeout):
        """
            Create a new Command object

            :param name: command name
            :param machine: object Machine where execute command
            :param command_line: string of command line
            :param timeout: timeout (in seconds) for command execution
            :return: Command instance
            :rtype: Command
        """
        self.name = name
        self.machine = machine
        self.command_line = command_line
        self.timeout = int(timeout) if timeout else 10

    def execute(self):
        """
            Execute this command 

            :return: return of the command
            :rtype: string
        """
        prompt = "[" + self.machine.username + "@" + self.machine.ip + "]"
        command_line = self.command_line
        print prompt + " " + command_line
        return self.machine.execute_command(self.command_line, self.timeout)

