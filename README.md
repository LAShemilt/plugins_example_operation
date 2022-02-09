# plugins_example_operation
How to write a minimal plugin framework for python, based on the game Operation
from Hasbaro. This is an educational example only.

## Introduction
Plugin Frameworks are extremely powerful and are a good way of structuring software, so that developers can easily extend the functional part without touching the main part of the code.

In this example we use the game operation as a model to provide an basis for our plugin structure. In the board game version, participants have use a pair of tweezers to extract plastic injuries from a compartments in a human form.
If the metal tweezers touch the sides of the compartment the patients nose flashes red and the game emits a buzzing sound. We aim to model this game in a simple software, and allow
for users to extend the game by writing plugins for new injuries for players to extract. 

## Software Structure
To model this in software our `core-software` package represents the board. This package contains the `play-operation` main method which assigns a player and surgery to perform, and 
tells a player if they were successful of not.  It also provides the structure of the operation a player will perform through the `Operation`  abstract base class. This class is formed
of two methods one is `remove_item` and the other is `buzzer_rings_when`. The `buzzer_rings_when` method is designed to emulate the touching of tweezers to the electrified container. It can be overwritten in any new operation to provide a conditional where the 
surgery was successful or not. The `play-operation` method asks a user for a number between 1-10, which is given to the `remove_item` method. This randomly selected number will
decide if the player was successful or not. 

The `core-software` package has a setup config defining entry points, one is the `play-operation` entry-point and the other is the `core_software.operations` entry point:
```
[options.entry_points]
core_software.operations =
    HammerToes = core_software.operations.hammer_toes:HammerToes
console_scripts =
    play-operation = core_software:play_operation
```
The `core-software.operation` entry-point allows the operations to be extended via plugins. All operations defined in this entry-point are automatically discoved in the `play_operation`
method in the core software using the `importlib` package:

```
     discovered_plugins = [ e.load()
     for e in importlib.metadata.entry_points()[
           "core_software.operations"
       ]]

```
This is used to find all plugins associated with the game.

## Writing a plugin
