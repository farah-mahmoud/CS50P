"""
This program calculates how much tip you should leave at a restaurant by inputting the meal price & tip you wanna leave
ex:

$ python tip.py
How much was the meal? $50.00
What percentage would you like to tip? 15%
Leave $7.50

"""
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    fl = d.replace('$', '')
    return float(fl)


def percent_to_float(p):
    num = p.replace('%', '')
    newnum = float(num)/100
    return newnum


main()
