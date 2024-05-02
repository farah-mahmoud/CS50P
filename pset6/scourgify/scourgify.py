# Problem Set6 (Scourgify): https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import sys
import csv

# making an empty dict
students = []

# usage: python scourgify.py before.csv after.csv
if len(sys.argv) == 3:
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # splitting the names into first and last
                last, first = row["name"].split(", ")
                # appending the names and house into the dict
                students.append({"first": first, "last": last, "house": row["house"]})

        # appending the names and house into the output csv file
        with open(sys.argv[2], "w") as csvfile2:
            writer = csv.DictWriter(csvfile2, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(
                    {
                        "first": student["first"],
                        "last": student["last"],
                        "house": student["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
# ex: python scourgify.py
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

# ex: python scourgify.py 1.csv 2.csv 3.csv
else:
    sys.exit("Too many command-line arguments")
