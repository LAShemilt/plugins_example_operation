from random import randint
import importlib
import pkgutil



def play_operation():
     discovered_plugins = [ e.load()
     for e in importlib.metadata.entry_points()[
           "core_software.operations"
       ]]

     # Select

     trigger = randint(0 , len(discovered_plugins)-1)

     operation = discovered_plugins[trigger]()
     print( f"The patient needs surgery on their {operation.name}")
     # select number
     num = int(input("Type in a number between 1-10:"))
     print("Your number is :", num)

     operation.remove_item(num)
