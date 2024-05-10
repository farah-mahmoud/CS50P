#https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
import sys

def main():
    while True:
        try:
            user_fraction = input("Fraction: ")
            converted = convert(user_fraction)

        except (ValueError, ZeroDivisionError):
            raise
            pass
        else:
            print(gauge(converted))
            sys.exit()


def convert(fraction):
    while True:
        try:
            n1, n2 = fraction.split("/")
            x, y = int(n1), int(n2)
            fuel = x/y * 100

        except (ValueError, ZeroDivisionError):
            raise
            break
        else:
            if x > y:
                break
            elif x <= y:
                return fuel
    main()

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return"F"
    else:
        return f"{round(percentage)}%"



if __name__ == "__main__":
    main()
