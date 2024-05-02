#https://cs50.harvard.edu/python/2022/psets/7/response/

from validator_collection import is_email
def main():
    email = input("Enter your Email: ")
    print(validate(email))


def validate(s):
    if is_email(s):
        return "valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
