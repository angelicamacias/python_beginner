class Cat: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person {self.name}, {self.age}years old."
    #The goal of the repr method is to be unambiguous.
    #If possible it should return a string that allows us to recreate the original object ver y easily 
    def __repr__(self):
        return f"<Person({self.name}m {self.age})>" #<> for say that is a string 



Gris: Cat 
Gris = Cat("Gris", 6)
print("Gris")
#here paythonis going to print out a string representing the Gris objects that we've created. 
#With that you can print out an object in case you want to recreate the object. 
    

Krity = Cat("Krity", 43)
print(Krity)   