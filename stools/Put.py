# -*- coding: utf-8 -*-

"""
    Module for put command
"""

from stools.Command import Command

class Put(Command):
    """
        Representation of a put command
    """

    def __init__(self, name, machine_source, machine_target, \
                 file_source, file_target):
        """
            Create a new Put object

            :param name: command name
            :param machine_source: object Machine where file_source is
            :param machine_target: object Machine where to put file
            :param file_source: name (or path) where file to put is
            :param file_target: name (or path) where put file
            :return: Put instance
            :rtype: Put
        """
        self.name = name
        self.machine_source = machine_source
        self.machine_target = machine_target
        self.file_source = file_source
        self.file_target = file_target
        self.command_line = "scp -r " + file_source + " " \
                                  + machine_target.username \
                                  + "@" + machine_target.ip \
                                  + ":" + file_target

    def execute(self):
        """
            Execute this command 

            :return: return of the command
            :rtype: string
        """
        prompt = "[" + self.machine_source.username \
                     + "@" \
                     + self.machine_source.ip \
                     + "]"
        command = self.command_line
        print prompt \
              + " " \
              + command
        return self.machine_source.execute_copy(command, \
                                                  self.machine_target)

