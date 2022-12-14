# PYTHON_BEGINNERS
Some instructions of the principal functions in python.

1. [Print function](#Print-function)
2. [Literals](#Literals)




## Print function 

The syntax for **print** function is:		

```python
print("Hello yellow cat")
```  

The arguments to a function are between parentheses the line is delimited with quotes, and a value between quotes is called a **string**.

The print function proviedes this possibilities:

- If we want to print multiple lines at once, we can do so by invoking multiple print functions:
```python
print("Hello yellow cat")
print("Helllo gray cat")

Hello yellow cat
Hello gray cat 
```
There can not be more than one instruction on a line in python 

- If we want to print a longer sentence taht should be separated with new lines, we can use the newline caracter **\n**
```python
print("Hello yellow \ncats")
Hello yellow 
cats 
```
###  Keyword argument for print function:

- **end** 
```python	
print("Hello!, end="")
print("yellow cat")

Hello! yellow cat 
```
This keyword argument determines the characters that the print functions sends to the output once it reaches the end of its positional arguments. Lines were printed
on the same line. 

- **sep** 

With sep we can control the how python separates the outputted arguments which is just a space by default. 
```python
print("Hello!, "yellow", "cat", sep="-")

Hello!-yellow-cat 
```
The same way we can cobining these the arguments and keywords for have the string that we want it:
```python
print("Hello, end="!"\n)
print("yellow cat", sept=WW, "end= :)")

Hello! 
yellowWW cat:) 
```
### ABSTRACT:
- Built-in functions: can be used without importing it.
- Allows us to print values to the console.
- We can invoke it with parentheses. 
- We can pass the value we want to print as arguments between the parentheses. 
- The backslash \ tells python that the next character has a special meaning (eg. \n).
- Keyword arguements such as sep and end can be used to format the output.

## Literals

A literal is data which values are determined by the literal it self:

```python
	200 "Hello!" "Python" -84
```

In python we can use literals in order to encode data and put them into your code. 

### Literals types

Are four types of literals:

- Integer
	- Octal numbers
	- Hexadecimal numbers
- Floating point numbers
- Strings
- Boolans 

- Integer 

The type integer, is a number that dosen't have a fraction

```python
	2000	125487	-90	1_000_000
```
There's also octal numbers

```python
 		0o1235
``` 
And the hexadecimal numbers 

```python 
		0x4587
```
- Floating point numbers 

This numbers have a nonempty decimal fraction 

```python 
	0.145		0.87		1e-22
```
- String

 A string is any series of characters that are interpreted literally by a script. 

```python
	"hello cat"  	"LKJH019283" 						
```
- Boolans

Bool is used to test whether the result of an expression is true or false.

```python
print(bool(expression))
```



# Python PCAP (associate programmer exam guide)

## MODULE:
A file containing python definitions and statements, wich can be later imported and used when necessary. 
- You own module
- Another deverloper's module
- Pyhon's built-in modules

--> math 
Math module is one of python's standard modules, and it provides us functions and classes to make it really easy to prerform mathematical calculations. 

--> dir 
A useful function when working with modules is the dir function. This function returns an anphabetically sorted list. 

--> Procedural 
Distinguishes data (variables) and code (modules and functions). Functions can use the data, but the data can not use the functions. 

--> Oject-Oriented
Data can code are enclosed together in classes. Objects exchange data and activate their meethods. 

 
```
first_vehicle = Vehicle()
```
 stack: is a data structure that follows the last-in-first-out approach or LIFO for short. A stack is an object with two methods push in order to put new elements on the top, and pop, to take the existing elements away from the top

push: we append the value that we pass through the function to the stack_list  
pop: we can remove those items and return them.

more that one stack:
Which means that you need to create another push and pop functions as well. 
For that we can create a class
    class:
class Vehicle:
    pass
we need to add a constructor function , to this function is to create a new object each time the class is invoked. The name of the constructor function is always init and it needs to have at least one parameter usually named self 

```
class stack:
    def __init__(self):
      print("I am in the constructor function!")
```
 
when a class component starts with two underscores, it becomes private. The property can, in that case, only be accessed from within the class. This is called encapsulation

The moset commonly used character number assignment is ASCII.
ASCII: American Standar code for information interchanged. 

