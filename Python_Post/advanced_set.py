A = {"Billy", "Blanquito", "Gris"}
B = {"Billy", "Gris"}


#it calls the difference functions inside friends. and this functions
#here takes another set, and what this'll do is it'll take this set ande remove from 
#it the elements in this set

local_friends = A.difference(B)
#if we put in this way:
#local_friends = friends_cats.difference(cats)
#we don't get anything because in base of friends_cats 
#comparting with "cats" don't have some different. 
print(local_friends)

#----------------------------------------------------
## Calculate the total with the function "union"
C = {"Manchitas", "Blanquito", "Krity"}
D = {"Billy", "Gris"}

total = D.union(C)
print(total)

#-----------------------------------------------------
## for know which elements are in the both sets we will use "intersection"
E = {"Billy", "Blanquito", "Gris"}
F = {"Billy", "Gris", "Manchitas", "Rocky"}

both = E.intersection(F)
print(both)