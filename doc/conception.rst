Conception
==========

.. uml:: 
   
   @startuml
   Configuration "1" *-- "*" Task
   Configuration "1" *-- "*" Machine
   Task "1" *-- "*" Command
   Command "1" -- "1" Machine
   Command <|-- Put
   Command <|-- Get

   class Configuration {
     +get_tasks_list()
     +get_task()
     +get_machines()
   }

   class Task {
     -name
     +execute()
   }

   class Command {
     -name
     -machine
     -command_line
     +execute()
   }

   class Put {
     -name
     -machine_source
     -machine_target
     -file_source
     -file_target
     +execute()
   }

   class Get {
     -name
     -machine_source
     -machine_target
     -file_source
     -file_target
     +execute()
   }

   class Machine {
     -name
     -ip
     -username
     -password
     -gateway
     +set_gateway()
     +execute_command()
   }
   @enduml
