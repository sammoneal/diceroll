# diceroll
# Final Group 1 - Dice Roll Project: Source Code

import random

while True: # Makes the code loop indefinitely 
  # Ask the user for the number of dice to roll
  num_dice = int(input("Enter the number of dice to roll: "))
  # If the user enters 0, terminate the program
  if num_dice == 0:
    break

  # Ask the user for the number of sides per die
  num_sides = int(input("Enter the number of sides per die: "))
  # If the user enters 0, terminate the program
  if num_sides == 0:
    break
  
  # Inititalize a list to hold the results of the dice rolls
  results = []

