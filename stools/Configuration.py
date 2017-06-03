# -*- coding: utf-8 -*-

"""
    Module for configuration file management
"""
import os
import sys
from configobj import ConfigObj, flatten_errors
from validate import Validator
from stools.Machine import Machine
from stools.Task import Task
from stools.Command import Command
from stools.Put import Put
from stools.Get import Get

class Configuration(object):
    """
        Class for configuration file management
    """
    @classmethod
    def get_configuration_from_file(cls, configuration_file):
        """
            Return a ConfigObj instance if configuration_file is validate

            :param configuration_file: filename of configuration file
            :return: ConfigObj instance
            :rtype: ConfigObj
        """
        configspec_file = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'spec', 'configuration.configspec')
        configuration = ConfigObj(configuration_file, configspec=configspec_file)
        validator = Validator()
        results = configuration.validate(validator, preserve_errors=True)
        if results != True:
            for (section_list, key, _) in flatten_errors(configuration, results):
                if key is not None: 
                    print 'The "%s" key in the section "%s" failed validation' % (key, ', '.join(section_list))
                else:
                    print 'The following section was missing:%s ' % ', '.join(section_list)
            sys.exit(2)

        return configuration

    @classmethod
    def get_tasks_list(cls, configuration_file):
        """
            Return list of all tasks configured in a configuration file

            :param configuration_file: filename of configuration file
            :return: Dictionary of tasks
            :rtype: dictionary
        """
        configuration = cls.get_configuration_from_file(configuration_file)
        tasks_dictionary = {}
        for category, configuration in configuration.iteritems():
            if category == "tasks":
                for task_name in configuration.iterkeys():
                    task = Task(task_name)
                    tasks_dictionary[task_name] = task
        return tasks_dictionary

    @classmethod
    def get_task(cls, configuration_file, task_name_to_search, arguments_list=''):
        """
            Get task instance of task_name_to_search configured in configuration_file

            :param configuration_file: filename of configuration file
            :param task_name_to_search: name of the task
            :return: Task instance of task_name_to_search
            :rtype: Task
        """
        configuration = cls.get_configuration_from_file(configuration_file)
        machines_dictionary = cls.get_machines(configuration_file)
        for category, configuration in configuration.iteritems():
            if category == "tasks":
                for task_name, task_configuration in configuration.iteritems():
                    if task_name == task_name_to_search:
                        task = Task(task_name)
                        argument_id = 0
                        for task_name, command_parameters in task_configuration.iteritems():
                            cls.replace_generic_commands(command_parameters, \
                                                         arguments_list, \
                                                         argument_id)
                            if command_parameters.get("type") == "put":
                                command = Put(task_name, \
                                               machines_dictionary.get(command_parameters.get("machine_source")), \
                                               machines_dictionary.get(command_parameters.get("machine_target")), \
                                               command_parameters.get("file_source"), \
                                               command_parameters.get("file_target"))
                            elif command_parameters.get("type") == "get":
                                                       command = Get(task_name, \
                                                       machines_dictionary.get(command_parameters.get("machine_source")), \
                                                       machines_dictionary.get(command_parameters.get("machine_target")), \
                                                       command_parameters.get("file_source"), \
                                                       command_parameters.get("file_target"))
                            else:
                                command = Command(task_name, \
                                                   machines_dictionary.get(command_parameters.get("machine")), \
                                                   command_parameters.get("command"), \
                                                   command_parameters.get("timeout"))
                            task.add_command(command)
                        return task

    @classmethod
    def replace_generic_commands(cls, \
                                 command_parameters, \
                                 arguments_list, \
                                 argument_id):
        """
            Replace generic argument

            :param command_parameters: list of parameters of command in configuration file
            :param arguments_list: list of arguments use with task name
            :param argument_id: current argument id
        """
        for argument in arguments_list:
            argument_id = argument_id + 1
            for parametre, valeur in command_parameters.iteritems():
                if valeur.find("$" + str(argument_id)) != -1:
                    command_parameters[parametre] = valeur.replace("$" + str(argument_id), argument)

    @classmethod
    def get_machines(cls, configuration_file):
        """
            Return list of all machines configured in a configuration file

            :param configuration_file: filename of configuration file
            :return: Dictionary of machines
            :rtype: dictionary
        """
        configuration = ConfigObj(configuration_file)
        machines_dictionary = {}
        for category, configuration in configuration.iteritems():
            if category == "machines":
                for machine_name, configuration_machine in configuration.iteritems():
                    machine = Machine(machine_name, \
                                      configuration_machine.get('ip'), \
                                      configuration_machine.get('username'), \
                                      configuration_machine.get('password'), \
                                      configuration_machine.get('gateway'), \
                                      configuration_machine.get('prompt'))
                    machines_dictionary[machine_name] = machine

                for machine_name, machine in machines_dictionary.iteritems():
                    gateway_machine_name = machine.gateway_machine_name
                    if gateway_machine_name != '':
                        gateway = machines_dictionary.get(gateway_machine_name)
                        machine.set_gateway(gateway)
        return machines_dictionary

