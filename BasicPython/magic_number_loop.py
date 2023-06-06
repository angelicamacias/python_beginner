#we want to repeat the game again and again. 
number = 7 

user_input = input("Enter 'y' if you would like to play: ")



while user_ != "n":

    # we want to execute this code allowing the user to guess a number, 
    # and then telling them whether it's wrong or not, for as long as the user didn't type n.   
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctyly")
    
    elif abs(number - user_number) == 1:
       
        print("You were off by one.")
    else: 
        print("Sorry, it's wrong!")


    user_input = input("Enter 'y' if you would like to play: ")