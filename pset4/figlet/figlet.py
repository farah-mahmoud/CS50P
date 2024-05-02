#https://cs50.harvard.edu/python/2022/psets/4/figlet/

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
if len(sys.argv) == 1:
    user_font = random.choice(figlet.getFonts())

elif len(sys.argv) == 3:
    if ("-f" == sys.argv[1] or "--font" == sys.argv[1]) and sys.argv[2] in figlet.getFonts():
        user_font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_text = input("Input: ")
f = Figlet(font=user_font)
print(f.renderText(user_text))
