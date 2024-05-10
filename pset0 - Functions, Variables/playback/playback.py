"""
Some people have a habit of lecturing speaking rather quickly,
and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed,
or even by having them pause between words.

-----------------
This program prompts the user for input
and then outputs that same input, replacing each space with ... (i.e., three periods).

"""

text = input("Enter Text: ")
new = text.replace(' ', '...')
print(new)
