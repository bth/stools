# -*- coding: utf-8 -*-

"""
    Module for machine
"""

import paramiko
import re, string

class Machine(object):
    """
        Representation of a machine
    """

    def __init__(self, name, ip, username, password, gateway="", prompt=None):
        """
            Create a new Machine object

            :param name: machine name
            :param ip: ip address (or hostname)
            :param username: username (login) for ssh connection
            :param password: password for ssh connection
            :param gateway_machine_name: machine name of gateway
            :param prompt: prompt to wait
            :return: Machine instance
            :rtype: Machine
        """
        self.name = name
        self.ip = ip
        self.username = username
        self.password = password
        self.gateway_machine_name = gateway
        if prompt == None:
            prompt = "[$#]+"
        self.prompt = prompt

    def set_gateway(self, gateway_machine):
        """
            Set gateway to access to this machine

            :param gateway_machine: instance of gateway machine
        """
        self.gateway = gateway_machine

    def create_connection(self):
        """
            Create SSH connection with this machine
        """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.ip, username=self.username, password=self.password)
        return client

    def write_on_terminal(self, terminal, string_to_write, string_of_end):
        """
            Write string_to_write on terminal and wait for string_of_end

            :param terminal: terminal instance
            :param string_to_write: string to write in terminal
            :param string_of_end: string of waiting
        """
        terminal.send(string_to_write + "\n")
        ret = ''
        while re.search(string_of_end, ret) == None:
            if re.search("Are you sure you want to continue connecting", ret):
                terminal.send("yes" + "\n")
            fragment = terminal.recv(9999)
            ret += fragment
        return ret

    def create_connection_by_terminal(self):
        """
            Create SSH connection with this machine with terminal
        """
        client = self.gateway.create_connection()
        terminal = client.invoke_shell()
        self.write_on_terminal(terminal, "ssh " + self.username + "@" + self.ip, "password: ")
        self.write_on_terminal(terminal, self.password, self.prompt)
        return client, terminal

    def execute_command(self, command):
        """
            Execute command on this machine

            :param command: command to execute
            :return: return of the command
            :rtype: String
        """
        if self.gateway == None:
            client = self.create_connection()
            stdin, stdout, stderr = client.exec_command(command, timeout=10)
            ret = stdout.readlines()
            ret = ''.join(ret)
            ret = ret[:string.rfind(ret, '\n')]
        else:
            client, terminal = self.create_connection_by_terminal()
            ret = self.write_on_terminal(terminal, command, self.prompt)
            ret = self.clean_output(ret)
        return ret

    def execute_copy(self, command, machine_target):
        """
            Execute copy command on this machine

            :param command: command copy to execute
            :param machine_target: machine instance of target machine
            :return: return of the command
            :rtype: String
        """
        if self.gateway == None:
            client = self.create_connection()
            terminal = client.invoke_shell()
        else:
            client, terminal = self.create_connection_by_terminal()
        self.write_on_terminal(terminal, command, "password: ")
        ret = self.write_on_terminal(terminal, machine_target.password, self.prompt)
        return self.clean_output(ret)

    def clean_output(self, output):
        """
            Delete useless space of output

            :param output: string to clean
            :return: cleaned string
            :rtype: String
        """
        cut_start = 0
        last_return_position = string.rfind(output, "\r\n")
        first_return_position = string.find(output, "\r\n")
        cut_start = first_return_position + 2
        output = output[cut_start:last_return_position]
        return output

