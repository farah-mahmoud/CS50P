# https://cs50.harvard.edu/python/2022/psets/3/taqueria/

felipes = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
felipes = {k.lower(): v for k, v in felipes.items()}
total = 0
while True:
    try:
        order = input("Item: ").lower()
        total = felipes[order] + total
    except KeyError:
        pass
    except EOFError:
        break
    print(f"Total: ${total:.2f}")



