# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    score = 0
    user_level = get_level()
    for question in range(10):
        x, y = generate_integer(user_level)
        answer = input(f"{x} + {y} = ")
        for tries in range(3):
            try:
                if int(answer) == x + y:  # correct
                    score += 1
                    break
                # if user answers wrong it asks again for 3 times and then shows the correct answer
                # and then moves on to the next question
                else:  # incorrect
                    print("EEE")
                    if tries == 2:
                        print((f"{x} + {y} = {x + y}"))
                        break
                    answer = input(f"{x} + {y} = ")

            # same as incorrect answers
            except ValueError:  # ((invalid value) cat or dog for ex
                print("EEE")
                if tries == 2:
                    print((f"{x} + {y} = {x + y}"))
                    break
                answer = input(f"{x} + {y} = ")

    print(f"Score: {score}")


def get_level():
    # asks for the level of difficulty of the game
    # if the user enters an invalid value (anything except 1, 2 or 3)
    # it reprompts again and again until entering a valid value
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    else:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)

    return X, Y


if __name__ == "__main__":
    main()
