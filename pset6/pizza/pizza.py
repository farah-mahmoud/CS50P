#Problem set6 (Pizza Py): https://cs50.harvard.edu/python/2022/psets/6/pizza/

from tabulate import tabulate
import csv
import sys

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            menu = tabulate(reader, headers="keys", tablefmt="grid")
        print(menu)

    #ex: python pizza.py hi
    except FileNotFoundError:
        sys.exit("File does not exist")
    #ex: python pizza.py hi.csv
    else:
        if sys.argv[1].endswith(".csv") == 0:
            sys.exit("Not a CSV File")

#ex: python pizza.py
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

#ex: python pizza.py foo bar
else:
    sys.exit("Too many command-line arguments")

