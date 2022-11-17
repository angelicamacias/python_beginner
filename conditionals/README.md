python

IF

if conditional 


syntax:


```python

if (conditional): 
 print("the conditional is true!")
```
dobles colons after the conditional "if" and for syntax is very imporant the space 
after the command "print" for indicate that this command is into the conditioal. 

We can add another conditonal with the keyword **else**, so if the first conditional 
is false then the conditional will work with the condition into the **else**.

```pytho
if (conditional):
 print("The condition is true!")
else:
 pirnt("The condition is false!")
```
Also we have another keyword **elif** we can use it in order to add another condition.

```python 
if (conditional):
 pirnt("The conditional is true!")
elif (conditional):
 pirnt("ONly the second conditional is true!")
else:
 print("Both conditions are flase!")
```

==========================================================================================
====================================================================================

WHILE

while condition: 

```
while (expression) :
    statement_1
    statement_2
    ....
```

With this condition you to execute code as long as a cerain condition is true. 



=========================================================================================
=====================================================================================

Loops-For


```
for i in range(10):
```

range: is responsible for generating all the desired values of the control variable

![for loop](https://user-images.githubusercontent.com/114703394/202341831-1242db27-f752-43f7-ae80-a25838e215b5.png)




-Objects of type int are not iterable instead a list, dictionary or a tuple should 
be used.

```python
x = 2021
for i in x:
  print(i)
```

![Imagen8](https://user-images.githubusercontent.com/114703394/202342242-d4d3b2c7-aac6-4419-8899-4f87904201c1.png)

=======================================================================================
=====================================================================================
====================================================================================
=======================================================================================


LOGIACAL OPERATORS


AND or Or keyword 


With the AND keyword, we can get a boolan value 

OR



Not


another logical operator, wich only takes one value 


buscar in internet the descriptions


=====================

Bitwise Operators



Bitwise Operators allow you to manipulate single bits of data, the first operator,
the ampersand is used for bitwise conjunction. 

The conjunction & operator only returns one if both bits are one, otherwise it returns
zero  

IMAGEEEN DIAPOSITIVA 11

```python
print (15 & 22)
 6
```

```python 
print (15 | 22)
31
```

```python 
print (15 ^ 22)
25
```


abstrac



- Logical operators **and** **not** and **or** return boolean values based on the 
passed values. 

- Bitwise operatos & | ^ and ~ allow us to manipulate single bits of data, and return 
0 or 1 based on the value of the bits that are used

- Bit shifting can be donde with the **<<** and **>>** operators. 


==========================================================================
=====================================================================

===List:




In a list each element is a scaler 


cats = ["Billy", "Krity", "Blanquito"]
 

each variable into the list have a possiton value 


```
               Billy       Krity       Blanquito 
possitions      0          1            2 
```

for print a specific  value we need to call it with the keyword it's means the name
of the list then, the possition of the data that we want. 

```
cats = ["Billy", "Krity", "Blanquito"]

print(cats[0])
 Billy

print(cats[1])
 Krity 

print(cats[2])
 Blanquito
```
in the same way we can call the values but using negative number: 


```
                         Billy       Krity       Blanquito 
negative possitions      -3         -2            -1 
```


We can changes oth the value selecting it and then declaring the new value: 

```python
cats = ["Billy", "Krity", "Blanquito"]

print(cats[0])= "Gris"
```

in the case that we don't have assigned a value por each possiton we will have 
a *indexError**
	


===> List-methods
Methods are specific kinds of functions, they be have lije a function ond look 
like it, but their purpose is a bit different. 
Two importans mehtos are: append and insert 

-list.append()

With the append method, we can ass a new item to the end of the list. 

```
cats = ["Billy", "Krity", "Blanquito"]

cats.append("Gris")

```
-list.insert()

With the insert method, we can insert a new item in a specific possition 

```
cats = ["Billy", "Krity", "Blanquito"]

cats.insert(2, "Gris")

```
we also have a **temp** keyword, with this we can chang the value of the 
first item in the list to have the value of the second item in the list.

```python 
 
cats = ["Billy", "Krity", "Blanquito"]
temp = cats [0]
cats[0] = cats [1]
cats[1] = temp 

```
after the assing the new possiton it will: 

```
temp= Billy

                     Krity     Billy    Blanquito 
positoincats            0        1          2
```

we can also write in only one line
 
```
cats [0], cats [1] = cats [1], cats [0]
```
- last.sort()
The sorth method sorts the array on which we invoke the method. By defualt, it sorts 
ascendingly from the lowest valu to the highest value 

```python 
catsages = [6, 7, 4, 11]
catsages.sort()
print(catsages)
4 6 7 11
```
the cats ages now from the lowest to the highest value. 


- last.reverse()


The revers method reverses all the elements in a list. The first item becomes 
the last item and the last item becomes the first item , 


```python 
catsages= [6, 7, 4, 11]
catsages.revers()
print(catsages)
11, 4, 7, 6
