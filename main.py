from user import User
import menu

if __name__ == "__main__":
    #Get the users detail
    username = input("Your username:   ")
    user = User.create_or_get_user_from_file(username)
    
    while True:
        
        menu.show_main_menu(user.username)
        user_input = input("***: ")
        if user_input.lower() == "a":
            #Creating a new task
            user.create_users_task()
            #Save it to the file
            user.write_json_file()
        elif user_input.lower() == "b":
            #User input search options
            while True:
                menu.show_search_menu()
                user_input = input("> ")
                if user_input == "a":
                    tasks = user.search_by_date()
                    user.display_tasks(tasks)
                elif user_input == "b":
                    tasks = user.search_by_time_spent()
                    user.display_tasks(tasks)
                elif user_input == "c":
                    tasks = user.search_by_keywords()
                    user.display_tasks(tasks)
                elif user_input == "d":
                    tasks = user.search_by_pattern()
                    user.display_tasks(tasks)
                elif user_input.lower() == "f":
                    break
                else:
                    print("Invalid Entry. Please retry!")
        elif user_input.lower() == "c":
            #Save your data to json before quitting
            user.write_json_file()
            print("Program is now closed, see you next time.")
            break
        else:
            print("Not a valid option, try another selection.")
