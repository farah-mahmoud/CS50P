# https://cs50.harvard.edu/python/2022/psets/6/shirt/

import sys
from PIL import Image, ImageOps
import os

#getting path and extension for both command-line arguments
path1 = sys.argv[1]
root1, ext1 = os.path.splitext(path1)

path2 = sys.argv[2]
root2, ext2 = os.path.splitext(path2)

#making sure it's case-insensitively as for example "jpg" is the same as "JPG"
e1, e2 = ext1.lower(), ext2.lower()

if len(sys.argv) == 3:
        if e1 != ".jpg" and e1 != ".jpeg" and e1 != ".png":
            sys.exit("Invalid Input")
        elif e2 != ".jpg" and e2 != ".jpeg" and e2 != ".png":
            sys.exit("Invalid Output")
        elif e1 != e2:
            sys.exit("Input and output have different extensions")

        else:
            try:

                # opening pics
                shirt = Image.open("shirt.png")
                before = Image.open(sys.argv[1])

                # Resizing the pic to fit the shirt
                before = ImageOps.fit(before, shirt.size)

                # pasting the shirt on the pic
                before.paste(shirt, shirt)

                # saving into "after_image"
                before.save(sys.argv[2])
                
            except FileNotFoundError:
                sys.exit("Input does not exist")


elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

else:
    sys.exit("Too many command-line arguments")
