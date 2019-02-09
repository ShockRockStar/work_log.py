from utils import clear_screen

def show_main_menu(username):
    #This will display the main menu for the user.
    
    welcome_txt = "What would you like to add, {}?".format(username)
    welcome_txt = welcome_txt.title()
    clear_screen()
    print("-"*len(welcome_txt))
    print(welcome_txt)
    print("-"*len(welcome_txt))
    print("""
          a.) Add a new Entry?
          b.) All current entries.
          c.) Quit the program.
          """)
    
def show_search_menu():
    #Display search menu to user
    clear_screen()
    print("-"*25)
    print("What would you like to search by?  ")
    print("-"*25)
    print("""
          a.) The Exact Date
          b.) The Time Spent
          c.) An Exact Search
          d.) The Regex Pattern
          e.) A Date Range
          f.) Return to Main Menu
          """)
