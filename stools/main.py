#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Entry point
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from argparse import ArgumentParser
from os.path import expanduser
from stools.Configuration import Configuration

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='0.1')
    parser.add_argument('-c', '--configuration', default=expanduser("~") + '/.stools/configuration.cfg')
    parser.add_argument('-e', '--execute', nargs='*')
    parser.add_argument('-l', '--log', default='ERROR')
    return parser.parse_args()

def main():
    """
        Entry point function
    """
    args = parse_args()
    logging.basicConfig(level=args.log, format='%(name)-10s: %(message)s')
    logging.info('Start')

    if args.execute != None:
        task_name = args.execute[0]
        arguments_list = args.execute[1:]
        task_to_execute = Configuration.get_task(args.configuration, task_name, arguments_list)
        if task_to_execute == None:
            print "Task " + task_name + " unknown."
        else:
            print "Execution of " + task_name + "..."
            task_to_execute.execute()
            
    if args.execute == None or task_to_execute == None:
        # Diplay all tasks
        list_tasks(args.configuration)

def list_tasks(configuration_file):
    print "Tasks:"
    tasks_dictionary = Configuration.get_tasks_list(configuration_file)
    for task_name in tasks_dictionary.keys():
        print "\t" + task_name

if __name__ == '__main__':
    main()

