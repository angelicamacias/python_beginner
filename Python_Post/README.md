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
