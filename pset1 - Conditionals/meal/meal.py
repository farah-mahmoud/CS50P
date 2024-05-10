"""
Suppose that you’re in a country where it’s customary to eat
breakfast between 7:00 and 8:00,
lunch between 12:00 and 13:00, and
dinner between 18:00 and 19:00.
 Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all.
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive.
For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below,
wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
convert should return 7.5 (i.e., 7.5 hours).
"""


def main():
    timenow = input("What time is it? ")
    if timenow.endswith("a.m.") or timenow.endswith("p.m."): #checking the format 24h or 12h
        converted = convert12(timenow)
    else:
        converted = convert(timenow)
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted<= 19:
        print("dinner time")


def convert(time):
    #11:50 --> 11.83
    hours, minutes = time.split(":")
    hour = int(hours) + int(minutes) / 60
    return hour
"""
If up for a challenge, optionally add support for 12-hour times, allowing the user to input times in these formats too:

#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.
"""
def convert12(time):
    clock, mode = time.split()
    hours, minutes = clock.split(":")
    if mode == "p.m." and int(hours) != 12:
        hours = int(hours) + 12
    hour = int(hours) + int(minutes) / 60
    return hour

if __name__ == "__main__":
    main()
