#While user input which should be equal to the input of menu is not equal to three, we 
#will then run this code here. 
#(1)While user input which is equal to whether input of menu is not equal to three 

from databases import create_table, add_entry, get_entries 
menu = """Plasee selec one of the following options:
1) Add new entry for today 
2) View entries. 
3) Exit. 

Your selection: 
"""

welcom = "Welcome to the programming diary!"
#add a new entry
def prompt_new_entry():
    entry_content = input("What have you learned today?")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)
    
#displaying entry information 1
def view_entries(entries):
    for entry in entries:
            print(f"{entry['date']}\n {entry['content']}\n\n")
        #we're using doble quotation marks at the end the start of the string.
        #The access of the data property in the dictionary must use single quotation marks
        #Otherwise, python would get confused.
    
print(welcom)

create_table()

while (user_input := input(menu)) != "3": #(1)
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, plase try again! ")