def divide(dividen, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")
        #If you raised an error the error happened, if you didn't raise the error the erro wouldn't have happend 
    return dividen / divisor

grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:   #as for create a alias
    print("There ar no grades yet in you list")
else:
    print(f"The avarage grade is {average}.")
finally: 
    print("Thank you!")
#if you wanna  run a pice of code always, no matte whether ther is an error, or no error. 
