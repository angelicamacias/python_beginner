number = [1, 3, 5]
doubled = [num * 2 for num in number]
 #How to we pyt each or these number (number list) multiplied by two, into 
 #this new list (dibled list)

print(doubled)

#=====if conditional in list commprehension ============

cats = ["Billy", "Numb", "Blanquito", "Krity"]
starts_s = [cat for cat in cats if cat.startswith("B") ]

#put what you wanna add to your new list so that's the variable cat 
#Then put the iteration or the for loo p
#for cat in cats:
#    if cat.startswith("B"):
#        starts_s.append(cat)

print(starts_s)
print(cats)
print(cats is starts_s)
print("cats:", id(cats), "starts_s: ", id(starts_s))
