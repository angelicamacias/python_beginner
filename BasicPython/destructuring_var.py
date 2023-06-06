student_attendance = { "Rolf": 96, "Juan": 100, "Angelica": 85}

print(list(student_attendance.items()))
# if we print this we get back is a list of tuples.


#insted of t, we can access it's components because we can destructure this 
# #into two separae variables.

                     # x, y = t 
        # sudent, attendance = sudent_attendance.items
#for student, arrendance in student_attendance.items():
 


# ============== another example tuple with three values ==================

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]


for name, age, profession in people: 
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# If one of the elements don't have three values then we will get an error: " ValueError"

#For that case we have an alternative using indixes. 


for person in people: 
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


#============= If you want to INGNORE a value into a tupple then: ============
head, *tail = [1, 2, 3, 4, 5]
#This syntax if for collecting. We are collecting all of the destructured values into the vaibale "*"
#So the first value get in the "head", the other will be in the variable "*tail"

print(head)
print(*tail)

# if we change the star to the variable "head"  then it collect all the values possible, but the last will be in the "tail" variable. 

*head, tail = [1, 2, 3, 4, 5]

print(*head)
print(tail)

