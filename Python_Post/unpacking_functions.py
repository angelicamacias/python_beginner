#stars: collect the arguments. 

def multiply(*args):
    print(args)
    total = 1 
    for arg in args:
        total = total * arg
    return total 

print(multiply(1, 3, 5))

#here is we've defined a function adn we've said, that the function has
# a set of arguments that will be collected into  a tuple of argument when the function gets called. 


#==============================================================

def add(x, y): 
    return x + y 

nums = [3, 5]
add(*nums)

#================================================================

def add(x, y): 
    return x + y 
nums = {"x": 15, "y": 25}
print(add(**nums)) #you've goy a dictionary with two keys 
# this is equal to ----> print(add(x=nums["x"], y=nums["y"]))


#================================================================

def multiply(*args):
    total = 1
    for arg in args: 
        total = total * arg 
    
    return total 
#if we multiply by a tuple you actually en up with that tuple 
#That means that args must be a tuple of tuples 
#Its becasue we don't pass an individual elements. 
def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else: 
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
#when we apply gunction we are passing in four different that are being collected into one tuple, by the star
#Why get a topple and not the multiplication of all the numbers? 
