Elements:
objects
Identifiers
Operators
Delimiters
Keywords
Comments
Blank Lines
White Space
Indentation 

example:

```
#All language elements are in this code 
a = 4
b = 5
c = [6, 7]

d = "Hi"
"Hello"

def area (x):
    return x**2
area (3)
____________
result= 9
```
Objects: 4, 5, [6, 7], 6, 7, "Hello", "HI", 
Function definition, 2, 3, 9
Comments: #All language elements are in this code 
Identifieres: a, b, c, d, area, x
Keyword: def, return 
Operators: **
Delimiters: = , " () : []
Blank lines
White space 
Identation 
=========================================================
What are the objects? 
The program displays a message to the user showing the coordinates of a rectangle. The user should enter the coordinates of a point. 
message: string 
coordinate: float
rectangle: ?
point: ?

==> Creating a class in python 

syntax 

```
class Point:
```
Use class and then you name the class that you want, ir your class has more than two words, you're use CamelCae 

This defines how a Point object looks like and what it dose:

```
class Point:
    def __init__(self, x, y):
    self.x = x
    self.y = y
```

Open parentheses and then you write the two required arguments that you need for a point to exist:
    
    create an instance of that type 
```
point1 = Point(10, 20) #object instance 
```
So here we called on object instance now of the Point type 
if you leave empty argumentes we will get a error. 

blueprint: id defines how a point object looks like and what it dose. 
constructor: Propiedad de una clase que te forza a pasarle un numero de parametros para poder instanciar un objeto a traves de ella miamooOOOoooor 