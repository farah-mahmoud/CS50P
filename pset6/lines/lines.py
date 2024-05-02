#https://cs50.harvard.edu/python/2022/psets/6/lines/
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as pythonfile:
            lines = 0
            for line in pythonfile:
                #if there's a comment or a blank line don't increment no. of lines
                if line.lstrip().startswith("#") == 0 and line.isspace() == 0:
                    lines += 1
            print(lines)
    except FileNotFoundError: #ex: python lines.py foo.py
        sys.exit("File does not exist")
    else:
        if sys.argv[1].endswith(".py") == 0:
            sys.exit("Not a Python file")
