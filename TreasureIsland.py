print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("Left or Right? ")
if direction == "Left":
      action = input("Swim or Wait? ")
      if action == "Wait":
          door = input("Which door? Red, Blue or Yellow.")
          if door == "Yellow":
              print("You Win!")
          elif door == "Red":
              print("Burned on fire. Game Over.")
          elif door == "Blue":
              print("Eaten by beasts. Game Over.")
          else:
              print("Game Over.")
      else:
          print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")