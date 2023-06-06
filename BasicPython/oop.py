# we're only defining how a student will behave 

class Student: 
    def __init__(self, name, grades):
    #accessing the name property inside of self 
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 90, 70, 80, 78))
student2 =  Student("Billy", (100, 90, 90, 60, 70))

print(student.name)
print(student.average())


print(student2.name)
print(student2.average())