#https://cs50.harvard.edu/python/2022/psets/7/watch/
import re
import sys


def main():
    print("URL: ", parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^<iframe(?:.+)?src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"(?:.+)?></iframe>", s, re.DOTALL):
        return "https://youtu.be/" + matches.group(1)
    else:
        return

if __name__ == "__main__":
    main()
