## __bases__
A tuple that contains the direct superclass of a certain class 
The basis property is a tool pool that contains direct superclasses of certain methods.  
## Since
It's a tool pool you can iterate the returned value of bases and extrac the name instaed. 
```
for base in Chihuahua.__bases__:
  print("Superclass name", base)
```
## Introspection 
The ability of a program to examine the type and properites of an object at runtime.

## Reflection 
The ability of a program to manipulate the values, properites, and methods of an object at runtime. This means that you don't have to know a complete class or object definition in order to manipulate this object. 

## __dict__
The class built-in __dict__ attribute shows all properties and methods of a class.

## Inheritance / Constructors

Passing attributes and methods from a superclass to a subclass

class Vehicle 
    move --> class WeeledVehicle
                     wheels---> Class car 

In computer programming, inheritance means passing attributes and methods from the superclass to a newly created subclass.

# multiple inheritance 
this ocurse when a class has more that one superclass

# Polymorphismo
tha ability to change the superclass' behavior. It can help the developer keep  code clean and consisten  
What is the difference between inheritance and composition?

# MOdule Resolution Order (MRO)
The way that a programming language scans through the upper part of a class's hierarchy in order to find the entity it currently needs.
It's essentially a set of rules that Python follows in order to determine from which class to use an entity when you invoke it. 

The way that MRO works is that it's algorithm scens to classes from bottom to top and from left to right. 

# Diamond problem
Is just something to be aware of when working with multiple inheritance. This problem arises when a subclass inherits from two superclasses that both inherit from the same class and override an entity defined on this class  