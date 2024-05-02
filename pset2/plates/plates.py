"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

rule 1 “All vanity plates must start with at least two letters.”
rule 2 “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
rule 3 “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
rule 4 “No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or
Invalid if it does not. Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #rule 2
    if len(s) > 6 or len(s) < 2:
        return False

    #rule 1
    if s[0].isalpha() == 0 or s[1].isalpha() == 0:
        return False

    for l in s:
        #rule 4 (no punctuation)
        if l.isalnum() == 0:
            return False

        #rule 3
        if l.isnumeric():
            if l == "0":
                return False
            if l.isalpha():
                return False

    return True

main()
