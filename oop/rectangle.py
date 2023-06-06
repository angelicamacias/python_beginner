import math 
from random import randint 
class Point:
    #The initialization method is a special method that is invoked automatically when an object is created by calling the class. 
    # The name of this method is __init__
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

#This will be replaced by the rectangle object, which has a low_left and upright
#We are goint to put a rectangle ther, which is going to be replaced by the rectangle
#object instance
    def falls_in_rectangle(self, rectangle):
        if  rectangle.low_left.x < self.x < rectangle.upright.x and rectangle.low_left.x < self.y < rectangle.upright.y:
            return True 
        else:
            return False

class Rectangle:
    def __init__(self, low_left, upright):
        #create the attributes of the rectangle
        #Self is the variable that holds the rectangle object. 
        self.low_left = low_left
        self.upright = upright

    def calculate_area(self):
        area = (self.upright.x - self.low_left.x) * (self.upright.y - self.low_left.y)
        return area

    def compare_area(self, area_user, area):
        if area == area_user:
            return True
        else:
            return False 


def area_user_guess():
    area_user = float(input("Guess the area:"))
    return area_user

def main():
    #The rectangle type is defined. 
    #To create a rectangular object instance we are referring to "Rectangle" type to create.
    #that object needs a low_left and upright point
    #low_left: randint(0, 9), uprigh: randint(0, 9) the same whit the next Point 
    #So  those two numbers produce the Point object, first Point and second.
    
    rectangle = Rectangle(
        Point(randint(0, 9), randint(0, 9)),
        Point(randint(10, 19), randint(10, 19)))


    #======> MASSAGE
    #create a massage to the user so it's printed out rectangle coordinetd
    print("Rectangle Coordinates:",
        rectangle.low_left.x, ",",
        rectangle.low_left.y, "and",
        rectangle.upright.x, ",",
        rectangle.upright.y)

    # We need to create a point object instance and we need to get the coordinated of that point from:
    user_point = Point(float(input("Guess X:")), 
                    float(input("Guess Y:")))

    print("Your point was inside rectangle:",
        user_point.falls_in_rectangle(rectangle))



    print(rectangle.compare_area(area_user_guess(), rectangle.calculate_area()))

    print("The area is ", rectangle.calculate_area() )

    #FLOWCHART: Generating a random rectangle and then asking for X and Y 
    #values and saying if that point is inside 
#is an idiomatic construc from python that uses some environment variables to give our programs a point of entry
if __name__ == "__main__":
    main()