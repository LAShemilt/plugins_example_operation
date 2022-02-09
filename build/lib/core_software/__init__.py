import plugins
from random import randint
import importlib
import pkgutil


def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def play_operation():
     discovered_plugins = {
          name: importlib.import_module(name)
          for finder, name, ispkg
          in iter_namespace(plugins)
     }

     # select number
     num = int(input("Type in a number between 1-10:"))
     print("Your number is :", num)

     # Select

     trigger = randint(0 , len(discovered_plugins))

     operation = [*discovered_plugins][trigger]

     discovered_plugins[operation].remove_item(num)
