from funny_bone import FunnyBone

def play_operation():

     # select number
     num = int(input("Type in a number between 1-10:"))
     print("Your number is :", num)

     # Select
     print("try to remove the funny bone")
     funny_bone = FunnyBone(num)
     funny_bone.remove_item()


if __name__ == "__main__":
    play_operation()