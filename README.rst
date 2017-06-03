======
stools
======

:Description: Tools for automate tasks on machines with only ssh
:License:     GPL
:Homepage:    http://entrecode.fr/stools/
:Development: https://github.com/bth/stools


What
----

"stools" is a module for Python 2.6+ that help you to automate tasks on machines
across network.

It is written entirely in Python.


Requirements
------------

- `Python <http://www.python.org/>`_ 2.6+
- `Paramiko <http://www.paramiko.org/>`_ 1.15+


Installing
----------

The recommended way to get `stools` is to download `archive file 
<https://github.com/bth/stools/blob/master/versions/stools-0.1.tar.gz?raw=true>`_ 
and install with `pip`::

    $ pip install stools-<version>.tar.gz

An alternative way is to extract archive::

    $ tar xvvf stools-<version>.tar.gz

Then, execute this commands::

    $ cd stools-<version>
    $ python setup.py install

Build
-----

You can build stools distribution with::

   $ python setup.py sdist

You can build documentation with::

   $ cd doc ; make html

Bugs & Support
--------------

:Bug Reports:  `Github <https://github.com/bth/stools/issues/>`_


