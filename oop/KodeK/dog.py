class Dog:
    def __init__(self, name):
        self.name = name
class Chihuahua(Dog):
    def __init__(self, name):
        Dog.__init__(self, name)
        self.size = "small"
        
for base in Chihuahua.__bases__:
  print("Superclass name", base)

pet1 = Dog("Max")


#if order to get a dictionary of all properites on a class.
#This property contains the name of the class. 
print(Chihuahua.__bases__)

#we can use them inside clasess of when using the type function
print(type(pet1).__name__)
#There's also the module property which stores the name of the module 
#that contains the definition of the class. 
print(pet1.__module__)