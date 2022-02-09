# plugins_example_operation
How to write a minimal plugin framework for python, based on the game Operation
from Hasbaro. This is an educational example only.

## Introduction
Plugin Frameworks are extremely powerful and are a good way of structuring software, so that developers can easily extend the functional part without touching the main part of the code.

In this example we use the game operation as a model to provide an basis for our plugin structure. In the board game version, participants have perform surgery by using a pair of tweezers to extract plastic injuries from compartments in a human form.
If the metal tweezers touch the sides of the compartment the patient's nose flashes red and the game emits a buzzing sound. We aim to model this game in a simple software, and allow for users to extend the game by writing plugins for new injuries.

## Software Structure
To model this in software, our `core-software` package represents the board. This package contains the `play-operation` main method which assigns a player and surgery to perform, and tells a player if they were successful of not.  It also provides the structure of the operation a player will perform through the `Operation`  abstract base class. This class is formed of two methods one is `remove_item` and the other is `buzzer_rings_when`. The `buzzer_rings_when` method is designed to emulate the touching of tweezers to the compartment edge. It can be overwritten in any new operation to provide a conditional where the surgery was successful or not. The `play-operation` method asks a user for a number between 1-10, which is given to the `remove_item` method. The player's choice of number will decide if the player was successful or not. 

The `core-software` package has a `setup.cfg` file defining entry points, one is the `play-operation` entry-point and the other is the `core_software.operations` entry point:
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
This is used to find all operation plugins and then uses them in the game.

## Writing a plugin

In the plugins package you will see examples of different operations used in the game. These plugins all extend the `Operation` abstract base class in the `core-software` package. As long as the plugins follow this pattern and have these methods, they can be executed in `core-software` without modifications to the code. 

In the plugins package there is a `setup.cfg` file. The setup of `plugins` requires that `core-software` be installed so that we can extend the `Operation` class
```
[options]
include_package_data = True
install_requires =
    core-software
packages = find:
python_requires =
    >= 3.9
```
In order to have our plugins included in the `core-software` package we have to add them in the setup.cfg under the `core_software.operations` entry point. 
```
[options.entry_points]
core_software.operations =
       TennisElbow = plugins.tennis_elbow:TennisElbow
       FunnyBone = plugins.funny_bone:FunnyBone

```

Plugins do not necessarily have to be added to the plugins package. You could develop your plugins as extra "Operation - Extension pack" in a package called `extension-pack`. As long as the extension pack meets the following criteria you will be able to use your plugins with `core-software`:
* Operation plugins extend the `Operation` abstract base class
* `core-software` is a dependency in the `setup.cfg` for the `extension_pack` package
* Operations are added as `core_software.operations` entry-points in the `setup.cfg`

## Installing the game
Clone the software locally
Create an environment with either `pip` or `conda`:
```
conda create -n operation-game
conda activate operation-game
```
Then install the packages in the environment:
```
cd core-software
pip install .
cd ../plugins
pip install .
```

You can then begin the game by typing in the console:
```
play-operation
```
You will be prompted to play. Have fun and enjoy:
```
play-operation
The patient needs surgery on their Funny Bone
Type in a number between 1-10:3
Your number is : 3
Removing Funny Bone
You extracted the funny bone successfully

```
