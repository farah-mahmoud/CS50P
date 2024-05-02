"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
 each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

"""
coin = 0
while coin < 50:
    new_coin = int(input("Insert Coin: "))
    if new_coin == 5 or new_coin == 10 or new_coin == 25:
        coin = new_coin + coin
    remaining = 50 - coin
    print(f"Amount Due: {remaining}")

if coin >= 50:
    owed = coin - 50
    print(f"Change Owed: {owed}")



