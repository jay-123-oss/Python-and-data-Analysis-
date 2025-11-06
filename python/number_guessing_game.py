import random

jacpot = random.randint(1,100)
guess = int(input("guess any number:  "))

count = 1

while guess != jacpot:
    if guess < jacpot:
        print("guess higher number: ")
    else:
        print("pleas, guess lower number:  ")
    guess = int(input("guess any number:  "))
    count+=1
print("correct guess, you win.")
print(f"you wim {count} atemt.")