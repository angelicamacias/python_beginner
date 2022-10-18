# PYTHON_BEGINNERS
Some instructions of the principal functions in python.

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
