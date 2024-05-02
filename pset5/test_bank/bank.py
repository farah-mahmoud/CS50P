#https://cs50.harvard.edu/python/2022/psets/5/test_bank/


def main():
    g = input("Greeting: ")
    print(value(f"${g}"))


def value(greeting):
    if greeting.strip().lower().startswith("hello"):
        return(0)
    elif greeting.lower().startswith("h"):
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()
