#https://cs50.harvard.edu/python/2022/psets/4/adieu/


names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break




#Version 1
#without using the inflect library (FROM SCRATCH)

print("\nAdieu, adieu, to ", end="")
k = 0
for n in names:
    if len(names) == 1:
        print(n, end="")
        break
    if len(names) == 2:
        print(f"{names[0]} and {names[1]}", end="")
        break
    elif k == len(names) - 1:
        print(f"and {n}", end="")
        break
    print(n, end=", ")
    k += 1
print()



#version 2
#using inflect library
"""
import inflect
p = inflect.engine()
mylist = p.join(names, final_sep="")
print(f"Adieu, adieu, to {mylist}")
"""
