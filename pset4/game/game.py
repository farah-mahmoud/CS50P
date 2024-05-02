#https://cs50.harvard.edu/python/2022/psets/4/game/

from random import randint

while True:
    try:
        level = int(input("Level: "))
        guess = randint(0, level)
    except ValueError:
        pass
    else:
        if level >= 0:
            break

while True:
    try:
        user_guess = int(input("Guess2: "))
        if user_guess < 0:
            pass
        elif user_guess < guess:
            print("Too small!")
        elif user_guess > guess:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass



