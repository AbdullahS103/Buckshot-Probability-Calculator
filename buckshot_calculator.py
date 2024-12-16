#!/usr/bin/env python3

def main():
  live_rounds = int(input("Enter number of live rounds : "))
  blank_rounds = int(input("Enter number of blank rounds : "))

  turn_counter = 1
  known_live_locations = set()
  known_blank_locations = set()

  while (turn_counter != live_rounds + blank_rounds):
    live_percentage = 0
    blank_percentage = 0

    if (turn_counter in known_live_locations):
      live_percentage = 100
      blank_percentage = 0
    elif (turn_counter in known_blank_locations):
      live_percentage = 0
      blank_percentage = 100
    else:
      live_percentage = (live_rounds / (live_rounds + blank_rounds)) * 100
      blank_percentage = (blank_rounds / (live_rounds + blank_rounds)) * 100

    print(f"Percentage of hit : {live_percentage}")
    print(f"Percentage of blank : {blank_percentage}")
    print()
    print("1. Populate Known Information")
    print("2. Populate Current Round Information")
    print("3. Advance Turn Counter")
    option = int(input("Enter option: "))
    print()

    if (option == 1):
      round = input("Enter type of round (L/B) : ")
      relative_turn = int(input("Enter turn of known information : "))
      if round == "L":
        known_live_locations.add(relative_turn + turn_counter)
      else:
        known_blank_locations.add(relative_turn + turn_counter)

    elif (option  == 2):
      round = input("Enter type of round (L/B) : ")
      if round == "L":
        known_live_locations.add(turn_counter)
      else:
        known_blank_locations.add(turn_counter)

    elif (option == 3):
      round = input("Enter type of round (L/B) :  ")
      if round == "L":
        live_rounds -= 1
      else:
        blank_rounds -= 1
      turn_counter += 1
    
    else:
      print("Invalid option, try again")

    print()
  
if __name__=="__main__":
  main()
