#we have a list with four user tuples 
#Inside it, they have an ID, a unque identifying number for each user a username and a password.  
users = [
    (0, "Billy", "password"),
    (1, "Gris", "gris123"),
    (2, "Krity", "krity2pass"),
    (3, "username", "1234"),
]

#we want to create a mapping of usernames to user information 
#In a dictionary comprehesion, the value that you're going to put into your new dictionary is 
# is actually a key value pair  


#is getting the user name and associting with it the entire user tupel 
username_mapping = {user[1]: user for user in users}


print(username_mapping)
#the keys are the username, ande the values are the entire tuple.

#you have the User's names and you want to ger their information out. 
#So you can acces just you've got the informarion out. 

print(username_mapping["Billy"]) 

#=====================================================================
 

username_input = input("Enter your username: ")
password_inpt = input("Enter your password: ")

_, username, password = username_mapping[username_input]

#and it's going yo unpack it, or de-structure it into these three variables 
#The undercore variable, because we don't care about the ID 
if password_inpt == password:
    print("Your details are correct!")
else: 
    print("Your detail are incorrect :c ")