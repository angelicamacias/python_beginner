class Animal:
    
    def __init__(self, type):
        self.type = type;

class Mammal(Animal):
    def __init__(self, animal):
        Animal.__init__(self, "mammal")
        self.animal = animal 

    def breathe(self):
        print("Breathing...")

class Dog(Mammal):
    
    def __init__(self, breed):
        Mammal.__init__(self, "dog")
        self.bread = breed
    
    def bark(self):
        print("Woof")


crocodile = Animal("reptile")
dolphin = Mammal("dolphin")
pet = Dog("Labrador")

print(dolphin.type) #tipo de clase 
print(dolphin.breathe())
print(pet.type)
print(pet.breathe())
print(pet.bark())

print(isinstance(pet, Dog)) #Pet is an instance of Dog which is a subclass of Mammal
print(isinstance(pet, Animal))
print(isinstance(dolphin, Dog))
print(isinstance(dolphin, Animal))