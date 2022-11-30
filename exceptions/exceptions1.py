x = int(input("Enter a number:"))

try:
    y = 1 / 0
    print(y)
except ZeroDivisionError:
    raise ZeroDivisionError("are you stupid?")