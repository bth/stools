.. stools documentation master file, created by
   sphinx-quickstart on Sun Dec 27 23:07:50 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to stools's documentation!
==================================

What
----

"stools" is a module for Python 2.6+ that help you to automate tasks on machines across network.

Example
-------

.. image:: img/example1.png
    :width: 300pt

For example, if you use `build` as a build machine, you can create a 
stools configuration file (:file:`~/.stools/configuration.cfg` on `my-pc`) like this:

.. code-block:: ini 

  [machines]
    
    [[my-pc]]
    ip = 192.168.1.1
    username = login
    password = passwd

    [[build]]
    ip = 192.168.1.2
    username = login
    password = passwd

  [tasks]
    
    [[build]]

        [[[update_and_build]]]
        machine = "build"
        command = "cd source_code_directory ; git pull ; make"
        
        [[[get_bin]]]
        type = "recovery"
        machine_source = "build"
        machine_target = "my-pc"
        file_source = "source_code_directory/bin"
        file_target = "~/bin"

On `my-pc` you can execute this task by using::

    $ stools -e build

Installing
------------

`stools` requires `Paramiko <http://www.paramiko.org>`_.

The recommended way to get `stools` is to download `archive file 
<https://github.com/bth/stools/blob/master/versions/stools-0.1.tar.gz?raw=true>`_ 
and install with `pip`::

    $ pip install stools-<version>.tar.gz

An alternative way is to extract archive::

    $ tar xvvf stools-<version>.tar.gz

Then, execute this command::

    $ cd stools-<version>
    $ python setup.py install

Documentation
-------------

.. toctree::
   conception

   autodoc

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

