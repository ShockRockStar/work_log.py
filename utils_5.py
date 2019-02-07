import os
import datetime

def clear_screen():
    """
    Clear the screen for Windows and other Operating Systems
    """
    os.system("cls" if os.name == "nt" else "clear")


def file_exists(filename):
    """
    Check if the users json file exists
    """
    return os.path.isfile(filename)

    
def get_date():
    date = None
    while not date:
        date_input = input("Please use MM/DD/YYYY:  ")
        try:
            date = datetime.datetime.strptime(date_input, "%m/%d/%Y")
        except ValueError:
            print("This is not a valid date, please try to enter it again.")
    return date

def convert_date_to_string(date):
    """
    Convert the date to a string to save in a json file
    """
    return date.strftime("%m/%d/%Y")

def convert_string_to_date(date_str):
    """
    Convert date in a string to datetime object
    """
    return datetime.datetime.strptime(date_str, "%m/%d/%Y")


def get_time_spent():
    """
    Check time_spent is a valid integer
    """
    time_spent = None
    while not time_spent:
        try:
            time_spent = int(input("Time spent(rounded minutes): "))
        except ValueError:
            print("That's not a valid number, Please enter the number of minutes spent on this task." )
    return time_spent