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

We can see in the Cat.py example where we are declaring a Cat type and we're doing basic programming logic (calling functions, iterating through objects, etc) with different objects instantiated from the Cat class.
Additionally, we're showing how importing a Point object point1 on a different file can help divide our code in different files while making use of the logic or data that is being produced there.


blueprint: id defines how a point object looks like and what it dose. 
constructor: Propiedad de una clase que te forza a pasarle un numero de parametros para poder instanciar un objeto a traves de ella miamooOOOoooor 

==> what is SELF?
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

Self in a class it the variable that holds the object isntance that is begin created by the class. 
So basically we are calling the function and we are passing the value to self x or y 

What we do this?: self.x = x

===> Creating a method 
cont: Count method counts the number of occurrences of a certain string in that string:
```
"john".count("j")
1
```
capitalize: Capitalize a string like 


__init__: it dosen't return anything and this methos, it's meant to initialize the objects you are creating with the type that you have. Is just to delcare what instance variable this object will have

```
def __init__(self, x, y):
    self.x = x
    self.y = y
```
for finds out if a cerain point with 

========================= HOUSE PAINT ===================================
FILE: house_paint.py 

Adding a Method
We decided to have a House class and a Paint class for our house painting cost calculator program. When we think of what classes we should have, we should also think about what responsibility each class will have. According to one of the software design principles, a class should have only one responsibility. In other words, we should avoid writing classes that do a lot of work. In our program, the responsibility of the House class will be the calculation of the number of paint buckets needed to paint the entire house and the responsibility of the Paint class will be the calculation of the total price of the paint.

Following the logic described above, your task for this exercise is to:

1. Add a paint_needed method to House

2. Let us suppose that 2.5 buckets of paint are needed to paint one square unit of a wall. Therefore, inside the paint_needed method you should multiply 2.5 with the self.wall_area and return the value. That value is the paint needed to paint the house.

======================== The rectangle class =========================
 In an effort to create a game where the user can guess a point in a rectangle by typing in some coordinates 
 So that points so far we came up with this point type, which has an X and Y coordinates to be defined to create an instance ot that point and also a fall_in_rectangle mehtod to check if the points, the instance of the point that was created, falls or not, in that rectangle. 
And we were able to excuete it like that. 



SETPS
First: Write all the types with their init functions. Think of the attributes frist, not the methods 


why don't use int?
We are using float to convert it because user input, when user types something it goes inside, Pyehon as a string, so we need to convert it to a number.  