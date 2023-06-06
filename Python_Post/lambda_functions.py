#gets some input and returns some output
print((lambda x, y : x + y)(5, 7))
 #This means we are using the next paramters in the function lambda 
# and print function for do something 


#return value of the fucntion but we don't specify the return keyword. 
#Lambda functions are used to return output so you don't need to specigy return because 


#If you want that the function lambda has a name then we have got the add variable 
add = lambda x, y: x + y 
# variable + lambda function + parametros + finally your return value without the return keyword


#map does is it foes over each value in the sequence such as list, a duble, a set, etc. 

def double(x): 
    return x * 2 



sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))
#It makes it a little bit cleare withour so many brackets 
#list: to print it out like a list, because the map function dosen't return a list of numbers. 