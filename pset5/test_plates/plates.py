#https://cs50.harvard.edu/python/2022/psets/5/test_plates/

#rule 1 “All vanity plates must start with at least two letters.”
#rule 2 “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#rule 3 “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
#AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#rule 4 “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #rule 2 (less than or equals 6 and greater than or equals 2)
    if len(s) > 6 or len(s) < 2:
        return False

    #rule 1 (must start with 2 letters at least)
    if s[0].isalpha() == 0 or s[1].isalpha() == 0:
        return False

    for l in s:
        #rule 4 (no punctuation)
        if l.isalnum() == 0:
            return False

        #rule 3 (no numbers except at the end & And can't start with a 0)
    for l in s:
        if s[-1].isnumeric() and s[0] != "0":
            return False

    return True

if __name__ == "__main__":
    main()
