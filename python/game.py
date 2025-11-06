# this is a rock paper scissor game with playing computer
while True:
    item = ["rock", "paper","scissor"]
    import random
    user_choice = input("enter your choice(ROCK/PAPER/SCISSOR): ")
    com_choice = random.choice(item)

    print(f"your choice is {user_choice} and computer choice is {com_choice}")

    if user_choice in item:
      
        if user_choice == com_choice:
            print("macth is tai ")
        elif user_choice == "rock":
            if com_choice == "paper":
              print("computer win")
            else:
              print("you win")
        elif user_choice == "papre":
          if com_choice == "rock":
            print("you win")
          else:
            print("computer is win")
            
        else:
         if com_choice == "paper":
            print("you win")
         else:
            print("computer is win ")




