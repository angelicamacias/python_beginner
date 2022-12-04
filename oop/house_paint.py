class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area
    
    def paint_needed(self):
        price = self.wall_area * 2.5
        return price

home1 = House(4)
print(home1.paint_needed())
        
class Paint:
    
    def __init__(self, buckets, color):
        
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

home1 = Paint(2, "white")
print(home1.total_price())