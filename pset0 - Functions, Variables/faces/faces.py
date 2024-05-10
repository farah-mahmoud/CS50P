"""
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face.
Nowadays, programs tend to convert emoticons to emoji automatically!

In this file called faces.py, There's a function called convert that accepts a str as input
and returns that same input with any :) converted to 🙂 and any :( converted to 🙁
All other text should be returned unchanged.

"""
def main():
    text = input("Enter Text: ")
    convert(text)

def convert(regular_emoji):
    emoji = regular_emoji.replace(':)', '🙂').replace(':(', '🙁')
    print(emoji)

main()
