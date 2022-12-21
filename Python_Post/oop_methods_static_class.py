class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

#All functions inside the class that use the object as the first parameter. 
#How would you call this method if you wanted to call it? 
#We have two options: 




    @classmethod  #is this will be the class itself. 
     #instead of the instance, or the object, self it actually takes a different parameter
     # Taht we usually in python, call cls.  
    def class_method(cls):
        print(f"Called class_method of {cls}")
    
    @staticmethod
    #dosen't have a parameter cls or self. 
    #These methods don't get enything when you call them 
    def static_method():




#-----> first option. Create a new objecto of type  ClassTest 
test = ClassTest()  #we are creating an object of tupe ClassTest or instance of ClassTest
test.instance_method()
#or
ClassTest.instance_method(test)


#-----> second option. 
ClassTest.class_method(ClassTest)
