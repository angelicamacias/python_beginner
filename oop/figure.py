import math 
class Point:
    #The initialization method is a special method that is invoked automatically when an object is created by calling the class. 
    # The name of this method is __init__
    def __init__(self, x, y):
        self.x = x 
        self.y = y 


    #keep in mind that don't use the same name that object type name in your methods, try to use verbs.  
    def falls_in_rectangle(self, lowleft, upright):
      
       #self is the variable that holds that will hold the object instance
        if  lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True 
        else:
            return False


        
    #Here we try to calculate the distance between one point and another point. 
    def dis_to_point(self, point):
        dis = math.sqrt(((self.x - point.x) ** 2) + ((self.y - point.y) ** 2))
        #We can put a point x or y because the arguement "point" have x and y 
        return dis 

point2 = Point(1, 1) #is 3 between 5-7 and 4 between 6-9?
point3 = Point(2, 2)

print(point2.dis_to_point(point3))
point2.falls_in_rectangle((5,6), (7, 9))
Point(3, 4).falls_in_rectangle((1, 1), (6,6))


# #we try to see if the x "coordiante" of our point  that we are going to create
# # is between the lower left, wich will be "point2" so self.x have to be between 
# # 5-7, ande self.y have to be between 6-9

##===================================

class Rectangle:
    
    def __init__(self, lowleft, upright):
        #create the attributes of the rectangle
        #Self is the variable that holds the rectangle object. 
        self.lowleft = lowleft
        self.upright = upright
        #The rectangle type is defined. 

#create a new point object
pointx = Point(6, 7)

#Create a rectangle object now Point(5, 6) it's a object and Point(7, 9) another object. 
rectanglex = Rectangle(Point(5, 6), Point(7, 9))
#here we just need to say "rectanglex" becasue this is alrady defined.
pointx.falls_in_rectangle(rectanglex)