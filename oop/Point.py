class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age 

def is_cat(object):
    if (type(object)) == Cat:
        return True

billy = Cat("Billy", "Orange", 11)
whitey = Cat("Blanquito", "White", 3)
krity = Cat("Krity", "White/gray", 6)
gris = Cat("Gris", "Gray", 9)

list_of_cats = []

list_of_cats.append(gris)
list_of_cats.append(krity)
list_of_cats.append(billy)
list_of_cats.append(whitey)


list_of_favorite_cats = []
index = 0 

for i in list_of_cats:
    if is_cat(i) and (i.name == "Billy" or i.name == "Blanquito"):
        list_of_favorite_cats.append(i)
        print(list_of_favorite_cats[index].name)
        index += 1




print(type(billy))
point1 = Point(10, 20)
print(type(point1))

print(is_cat(krity))

