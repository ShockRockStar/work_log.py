# work_log.py
This is a terminal application for employee work logs. It asks what someone did on a certain day. 
This project asks for a task name, 
how much time was spent on said task, 
and any additional notes the user would like to add to the task. 


The main file requests a user name, runs the function, and runs the while loop looking for user input
based on "adding new items", "Searching for all existing entries", and "Exiting the Program."
The system will check if a user name exists and it not it will store the user name in a json file. 
If the username exists it will retrieve the user data from json. 

with main file open, menu will display main_menu. This will ask you what you would like to do. 


If you want to add an item (input "a") the program will call the user file and the function, create_users_task.
The screen will first clear.
It will print "Date of the task". 
The program will then prompt the user from the utils file to Enter the date using DD/MM/YYY format.
utils.get_date() will check if the input is entered in the correct %d/%m%Y format. if not, the program will print
"That's not a valid date. please try again."
After the user enters a proper date the program will then ask the user to input "Title of the Task: "
This is then cleared.
Next, the program will prompt you to enter the Time Spent on the task that needs to be completed.
We pull this function from utils and call get_time_spent()
In utils.get_time_spent() the program is asking for an integer input of time needed for the task (rounded).
ValueError checks if a user enters something other than an integer.
Screen is cleared. 
Next, the program checks if the user wants to add notes to their worklog.
Notes are stored in the Notes variable.
Screen is cleared.
Task is successfully logged.
The task is simultaneaously logged to a json file. 

If user selects choice "b" from the main menu, they can search all entries.
Once "b" is selected menu.show_search_menu(): will display:
a.)Exact Date
b.) Time Spent
c.) Exact Search
d.) Regex Pattern
e.) Date Range
f.) Return to main menu

main file lists all the while loop selections for the main menu choices.


If user selects choice "c", the program will write and save whatever information the user was working on prior to exiting to user.write_json_file()



