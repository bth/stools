.. stools documentation master file, created by
   sphinx-quickstart on Sun Dec 27 23:07:50 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: ../README.rst

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
        type = "get"
        machine_source = "build"
        machine_target = "my-pc"
        file_source = "source_code_directory/bin"
        file_target = "~/bin"

On `my-pc` you can execute this task by using::

    $ stools -e build

Use
---

For list all configured tasks, you can do::

    $ stools

By default, `stools` search config file as `~/.stools/configuration.cfg` but 
you can specify where is your configuration file by using::

    $ stools -c /my_path/my_configuration.cfg

You can execute a task `my_task` by using::

    $ stools -e my_task

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

