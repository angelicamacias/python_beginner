from geometry import Point
point5 = PPoint(100, 200)
print(type(point5)) #The result is the file where this PPoint is located.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        print(self) #we can see that we will get 4 results form this print 


point1 = Point (10, 20)
point2 = Point (12, 22)
point3 = Point (13, 23)
point4 = Point (13, 23)

number1 = int("2")
print(type(point1)) #The result is actually the name of the current script 
print(point1)   #The result of this is weird, but Python dosen't know what this is a pint object. 
#we need to give some special instuctions inside the class defenition for see the point object.
#we have to create a new method here for pyhom can to display the inofrmation. 
print(number1)
print(point1.x)
