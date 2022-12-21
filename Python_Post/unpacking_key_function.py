
#unpack a dictionary into keyword arguments. 
#**= collect keyword arguments
def named(**kwargs):
    print(kwargs)

#we get out is a dictionary    
named(name="Bob", age=25)
#dictionary key is equal to the name of the keyword argument. 

#the same way we can unpack a dictionary into named arguments. 

def named(name, age):
    print(name, age)

#defined ditalls: 

details = {"name": "Gris", "age": 6}

named(**details) #**= collect keyword arguments
#if we use ** it treats the key as the name for the argument, and age as the key for the argument. 
# and assigns to them the value associated with those 

#===============     NICE     FORMAT      ==============

def print_nicely(**kwargs):
    named(**kwargs)
#getting arg and value for each item in the dictionary 
    for arg, value in kwargs.items():   #kwargs is a dictionary so we can use the items method on it. 
        print(f"{arg}: {value}")

print_nicely(name="Gris", age=6)#we are going to collect these named arguemnts into this dictionary. 
DD

#========================== use both =========================
#This syntax is normally used to accept an unilimted number of arguments. 

def both(*args, **kwargs):
    print(args)
    print(kwargs)
both(1, 3, 5, name="Blanquito", age=3)

# *args will collect the values 1,3,5 because they are positional arguments. 
# ** kwargs: will be collect name and age 


#============================= MAPPING ==========================

def myfunction(**kwargs):
    print(kwargs)

myfunction(**"Gris") #erro, must be mapping 
myfunction(**None) #error

#sometimes the variables that we use may not be what we expect. 

