#This tells python is that this thing should be a list 
#-> this function is going to return a float. 
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)

#=====================================================================
from typing import List

class Book: 
    pass


class BookShelf: 
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


#if that you'll get told ir you pass in the wrong thing 

