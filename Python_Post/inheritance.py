class Device: 
    def __init__(self, name, connected_by ):
        self.name = name
        self.connected_by = connected_by
        self.connected = True 


#!r: calls thee repr method of self.name that it shows up as having the quotes alredy. 

    def __str__(self): 
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False 
        print("Disconnecte.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        #it's going to call the init method of that super class
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.ramining_pages = capacity
        # Whay am i doing two properties with the same value? 
#The capacity is the maximum amount of pages that a printer could potentially print 
     
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaing)"
        #And then we're also going to input in self.remaining pages. 
    def print(self, pages): 
        if not self.connected: 
            print("Your printer is not connected!")
            return 
        print("Printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)


        