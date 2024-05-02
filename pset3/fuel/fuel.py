#https://cs50.harvard.edu/python/2022/psets/3/fuel/

while True:
    try:
        fraction = input("Fraction: ")
        X, Y = fraction.split("/")
        x, y = int(X), int(Y)
        fuel = x/y * 100


    except (ValueError, ZeroDivisionError):
        pass
    else:
        if x <= y:
            break

if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(f"{round(fuel)}%")

