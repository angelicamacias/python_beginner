## List, tuples and sets
Multiple values in the same variable. 

### --> List
List is defined by using squer brakets, into the squer brakets you can put differents values separated by comma. 
```
l = ["billy", "blanquito", "gris"]
```
> for print a individual values 
``` 
  l = [0]
  billy
```
> for modifay a value

```
l = [0] = "manchitas"
pirnt(l)
["manchitas", "blanquito", "gris"]
```
> for add a new element 

```
l.append[krity]
print(l)
["manchitas", "blanquito", "gris", "krity"]
```
NOTA: append= add at the end

> for remove a new element
```
l.remuve("blaquito")
print(l)
["manchitas", "blanquito", "gris", "krity"]
```

### ---> Tuples 
Tuples difined by using parenthese. We can;t modify a tuple, you can add and remuve. 

NOTE: Lists and tuples keep the order of the elements. 

MODIFAY: Tupes can not be modified after they're created. 

append: the tuple object has no attribute append. We can't add things or remove ehigs from a tuple. 

### ---> Set

```
s = ["billy", "blanquito", "gris"]
```

Set is defined by using squer or nomal brakets. The difference between a set and the other two is that while you can add and remove element from a set you can't have duplicate elements. 
Sets don't necessarily  keep the order. The values can changes in any moment. 
You can't print indivual values because they changes of possition

> add a element
for set we can use a "add".
Sets don't have an "end" since they don't have order. 
```
s.add("Krity")
pirnt(s)
["billy", "blanquito", "krity", "gris"]
```
NOTE: The element can't be duplicate. 

## Advanced set operations
Proyect --> advced 
difference: the differents element in two sets. 
intersection: The equal ements in two sets
union: all the elements on two sets

## The in keyword
Proyect --> magic_number.py 

With keyword "in" we can check is one thing is inside a list or a tuple or a set. 

NOTE: That it dosen't habe to be a tuple anything where the "in" keyword would work, works as well. 

## Loops 
Proyect --> magic_number_loop.py
We have tow types of loop 
- One that allows us to repeat some code a certain number of time. 
- One that allows us to repeat code for as long as a condition is true. 

## List  comprehesion 
Proyect ---> list_comprehesion.py
 A list comprehesion is a great feature of pyhon and allows us to create new lists on the fly form existing lists.

 ## Dictionaries 
Proyect ---> dictionaries 
 Dictionaries are for is to associate keys and values together so that ir you know the key 

 ## Destructuring variables 

 The brackets are only needed when you want to explicitly say, i want a tuple here, i don't want python to trea these as two separate values. 

 https://blog.teclado.com/destructuring-in-python/


## Functions in python 

 function body :
  def hello (): 
    pirnt ("hello!")

  function has been defined, but the function has not been called. 

  hello ()

Things that you should not do in functions 
- re-use names 

example 1: 
```
  def print():
      print("Don't do this")
```

example 2: 
```
friends = ["Rolf", "Bob"]

 def add_friend():
    friend_name = input("Enter your friend name: ")
    friend = friend + [friend_name]
```
WE can't do that, because you can't use a variable in the same line where you're definig it. 

- Use them before they get defined. 

## Function agrguments and parameters 
The next function have two parameters: 

def add(x, y): 
   pass 
pass: do nothing 

What happens is that when python runs the function, when you call the function itself, this two variables are created and the function can use them inside the function body. When you get to the end of the function body, the variables disappear. 


ARGUMENTS: Provdes a value to one parameter in this case: 
```
def add(x, y):
   pass

add (5, 4)
```
Five is the value of x, and three will be the value of y. 

If the function don't have any parameter then we can't give it any argument. 
But if the function have parameter we need to give it an argument. 

## Defaul function paramter values 

```
def add(x, y=8):
  print(x + y)

add(5) 
  or
add(x=5)
```
We can give to the arguments a value, WITHOUT spaces.
So if you don't give a argument when you call the function then by default the function take the value 8 for y.

NOT TO DO THIS
```
default_y = 3

def add(x, y=default_y):
  sum = x + y
  pirnt(sum)
```
Parameter equal to our defualt_y variable. 

## Lambda functions 

Lambda function is a different type of function which dosen't have a name and is only used to return values. 
Lambd functions are exlusively used to operate on inputs and return outputs. 
They are almost never used to perform actions. 
```
lambda x, y = x + y
```
- Ofen used without giving them a name 
- Can give them a name by assinging them to a variable. 
- They are used to return a value calculated from it's parameters 
- They're almost never used to perform actions. 
- They're almost always single line. 

## Map

Map function dosen't return a list of numbers, it will return something called a map object. 

## Dictionary comprehesions
--> dictionary_comprehesion.py
- Imagine you know a user's 


## Unpacking function arguments 
--> unpacking functions

## Unpacking keyword arguments

** = collects keyword arguments. 

## Object-Oriented programming 

Allowing us to write codce that looks like what we would work with in the real world. 
** Class: ** Defenetion of something 

## Magic methods: __str__ and __repr__

## Class methods and static methods 

Instance methods: Instance method need the object in order to call them.
Class method: Here you can define another method. 
Gets the class normally
static mehtods: Don't get either of those things. 
If you want a function iside the class that dosen't use the class for anything, or the instance, you can decorate it eith @staticmethod. 

If you want a method that uses the class for something then you can decorate it @classmethod. 

What are these used for? 
When you wanna produce an action that uses the data inside the object that you created earlier.
If you wanna calla method to modify some sort of data inside self or the object. 

 ## Class inheritance 
 Inhertiance allows one class to take some methods and properties from another class. 

 ## Class composition 
 
 Compossition is a counterpart to inheritance. In addition, composition means something different. 
 When you do inheritance, you are essentially treating it like evolutionary inheritance. 
 Composstion if for when you wanna say something like a bookchelf has many books. A bookshelf is composed of a bunch of things and books. 

This is helpful when you have a class that contains a bunch or other classes or a class. 

## Type hinting

Type hinting is a new feature in Python 3.5 

## Importing in python 
--> directory importing 

## Relative imports 

Is one that can import from the current folder that the file is in. But it can not import unless there is a folder name in the import path, in the module path. 

## Errors 
 
Error are often used for flow control very much kike if statemnts. By allowing your functions to raise errors you're going to then be able to catch them in your code and handle them . 

Exception and error are the same things
 - Error help you track down problems 
 - Where and why they happened. 

## Custom error classes in python 


## Class functions 

In first-class function, just means that functions are just variables. 
And you can pass them in as arguments to functions and use them in the same way you would use any other variable. 
