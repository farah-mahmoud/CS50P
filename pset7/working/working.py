#https://cs50.harvard.edu/python/2022/psets/7/working/
import re
import sys

def main():
    print(convert(input("Hours: ")))
#Goal
#9:00 AM to 5:00 PM
#Or
#9 AM to 5 PM -> 09:00 to 17:00

#hours(either AM or PM): 12 1 2 3 4 5 6 7 8 9 10 11
#1-12 -> 1-9 then 10-12
#minutes: 00 01 02... 60
#0-59 -> 0-9 then 10-59
def convert(s):
    if matches := re.search(r"([1-9]|1[0-2]):?([0-5][0-9])?\ (A|P)M\ to\ ([1-9]|1[0-2]):?([0-5][0-9])?\ (A|P)M", s, re.IGNORECASE):
        h1, h2 = int(matches.group(1)), int(matches.group(4))
        m1, m2 = matches.group(2), matches.group(5)
        if m1 == None:
            m1 = '00'
        if m2 == None:
            m2 = '00'
        #AM to PM
        if matches.group(3) == 'A' and matches.group(6) == 'P':
            #converting AM
            if h1 != 12:
                h1 = f"{h1:02}"
            else:
                h1 = '00'

            #converting PM
            if h2 != 12:
                h2 += 12

            return f"{h1}:{m1} to {h2}:{m2}"

        #PM to AM
        elif matches.group(3) == 'P' and matches.group(6) == 'A':

            #converting AM
            if h2 != 12:
                h2 = f"{h2:02}"
            else:
                h2 = '00'

            #converting PM
            if h1 != 12:
                h1 += 12

            return f"{h1}:{m1} to {h2}:{m2}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
