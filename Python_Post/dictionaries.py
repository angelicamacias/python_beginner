cats_ages = {"Billy": 7, "Krity": 5, "Blnaquito": 3}
#if you wante to access one particular element. 
print(cats_ages["Billy"])


#For change a element: 

cats_ages["Krity"] = 20
print(cats_ages["Krity"])

#================= another index with more elements =================== 
friends = [
    {"name": "Billy", "age": 26},
    {"name": "Gris", "age": 23},
    {"name": "Krity", "age": 30},
]

#for get a item 
print(friends[1])
#for get the name from a item 
print(friends[1]["name"])
#for get the age form a item 
print(friends[2]["age"])

#===================== dicionary with for loop ===================

student_attendance = { "Rolf": 96, "Juan": 100, "Angelica": 85}

#Which will print out the student variable which is the students name
#and then you can acccess the student key in the student attendance dictionary 
#using subscript notation to get their attendance. 

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

#======== other way 
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
# we have got here is that student attendance dot items gives us two values for
#each student, taht you can get as two separate variables here in python


# "in"  keyword in a dictionary to check whether a value is one of the keys of the dictionary

if "Juan" in student_attendance:
    print(f"Juan: {student_attendance['Juan']}")
else: 
    "Juan is not a student in this class."

# Calcule an average. 

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

#here we add 96+100+85 together and divide by three
#.values for get only the number 