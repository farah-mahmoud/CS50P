#https://cs50.harvard.edu/python/2022/psets/7/um/
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\W*\bum\b\W*", s, re.IGNORECASE)
    counts = len(matches)
    return counts


if __name__ == "__main__":
    main()
