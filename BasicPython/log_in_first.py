users = [
    (0, "Billy", "password"),
    (1, "Gris", "gris123"),
    (2, "Krity", "krity2pass"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else: 
    print("Your detail are incorrect :c ")