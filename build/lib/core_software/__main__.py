from .funny_bone import FunnyBone
from .tennis_elbow import TennisElbow
from random import randint

def play_operation():

     # select number
     num = int(input("Type in a number between 1-10:"))
     print("Your number is :", num)

     # Select

     trigger = randint(0 , 1)

     if trigger == 0:
          print("try to remove the funny bone")
          FunnyBone().remove_item(num)
     elif trigger == 1:
          print("try to remove Tennis Elbow")
          TennisElbow().remove_item(num)

if __name__ == "__main__":
    play_operation()