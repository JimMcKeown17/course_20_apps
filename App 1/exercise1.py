from random import randint

while True:
    try:
        lower = int(input("Enter the Lower Bound: "))
        upper = int(input("Enter the Upper Bound: "))
        print(randint(lower, upper))
        break
    except ValueError:
        print("Enter a number.")
        continue