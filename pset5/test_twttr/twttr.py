#https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    vowels = ['a', 'A', 'E', 'e', 'i', 'I', 'o', 'O', 'u', 'U']
    for vowel in vowels:
        word = word.replace(vowel, '')

    return word

if __name__ == "__main__":
    main()
