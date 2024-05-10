#https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #ex: #.#.#.#
    #each # should be 0-255
    #0-199 -> [01]?[0-9][0-9]?
    #200-249 -> 2[0-4][0-9]
    #249-255 -> 25[0-5]
    #{3} means repeat this 3 times just for simplicity of this line of code
    if re.search(r"^(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
