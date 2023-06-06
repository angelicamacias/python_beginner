#magic number a hidden number from the user 
#we're going to ask the user to enter a number
#Then we are going to tell the user  whether they got the number rigth or not. 
#Befote we do that we're going to ask the user whether they want to play the game or not. 

number = 7 

user_input = input("Enter 'y' if you would like to play: ")
#user_input = input("Enter 'y' if you would like to play: ").lower()
# for the case that the user use capital letter we use the option "lowe"
#the other way is using keyword "in"


if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctyly")
        #if the reuslt of number - user number is equal 1 or -1 then: 
    elif number - user_number in (1, -1):
        # abs(number - user_number) == 1:   we are converting the difference in absolut number, for that we equalize the result to 1 
        print("You were off by one.")
    else: 
        print("Sorry, it's wrong!")
