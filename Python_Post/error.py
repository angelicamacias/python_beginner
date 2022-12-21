def divide(dividen, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")
        
    return dividen / divisor

grades = []

print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"The avarage grade is {average}.")