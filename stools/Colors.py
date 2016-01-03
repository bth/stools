# -*- coding: utf-8 -*-

"""
    Module for colors management in terminal
"""

class Colors(object):
    """
        Classe for colors management in terminal
    """

    @classmethod
    def enable_color(cls, color):
        """
            :param color: color name
            :return: string for enable color in terminal
            :rtype: string
        """
        colors_dictionary = {"black"  : "0", \
                             "red"    : "1", \
                             "green"  : "2", \
                             "yellow" : "3", \
                             "blue"   : "4", \
                             "pink"   : "5", \
                             "cyan"   : "6", \
                             "white"  : "7"}
        prefix = "\033[9"
        suffix = "m"
        return prefix + colors_dictionary.get(color) + suffix

    @classmethod
    def disable_color(cls):
        """
            :return: string for disable color in terminal
            :rtype: string
        """
        return "\033[0m"

