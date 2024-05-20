# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions & classes with structured error handling
# Change Log:
#   aliciad, 05/16/2024, Created script
# ------------------------------------------------------------------------------------------ #

import json
from sys import exit

# Constants and global variables
MENU: str = """
    ---- Course Registration Program ----
    Select from the following menu:
    1. Register a student for the course
    2. Show current data
    3. Save data to file
    4. Exit the program
    -------------------------------------
"""
FILE_NAME: str = "enrollments.json"

menu_choice: str = ""
students: list = []


# Data Layer / File processing block
class FileProcessor:
    """Class to handle data storage and retrieval"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Read file and load to json and return list"""
        
        try:
            with open(file_name) as file:
                student_data = json.load(file)
        except FileNotFoundError as error_message:
            IO.output_error_messages("\nFile not found.", error_message)
        except Exception as error_message:
            IO.output_error_messages("\nUnknown Error. Please contact support. ", error_message)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Write data to json file"""
        
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
        except FileNotFoundError as error_message:
            IO.output_error_messages("\nFile not found.", error_message)
        except Exception as error_message:
            IO.output_error_messages("\nUnknown Error. Please contact support.", error_message)


# Presentation Layer / IO block
class IO:
    """Class to handle user input and output"""
    
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Standardized error messages for program"""
        
        print(message, end="\n\n")
        if error is not None:
            print("--- Error Details ---")
            print(error, error.__doc__, type(error), sep="\n")
    
    @staticmethod
    def output_menu(menu: str):
        """Display menu options to user"""
        
        print(menu, end="\n\n")

    @staticmethod
    def input_menu_choice():
        """Process user's menu choice"""

        choice = "0"
        try:
            choice = input("Choose a menu option (1-4): ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Invalid option.  Please choose between 1-4.")
        except Exception as error_message:
            IO.output_error_messages("\nUnknown Error.", error_message)
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """Process user's input and append to dictionary"""
        
        try:
            student_first_name = input("Enter the student's first name: ")
            if len(student_first_name) == 0:
                raise ValueError("First name can't be empty.")
            if not student_first_name.isalpha():
                raise ValueError("First name can't contain non-alphanumeric values.")
            student_last_name = input("Enter the student's last name: ")
            if len(student_last_name) == 0:
                raise ValueError("Last name can't be empty.")
            if not student_last_name.isalpha():
                raise ValueError("Last name can't contain non-alphanumeric values.")
            course_name = input("Enter the course name: ")
            if len(course_name) == 0:
                raise ValueError("Course name can't be empty.")
            student = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as error_message:
            IO.output_error_messages("\nInvalid Entry.  See details below.", error_message)
        except Exception as error_message:
            IO.output_error_messages("\nUnknown Error. Please contact support.", error_message)

    @staticmethod
    def output_student_courses(student_data: list):
        """Output current data to user"""

        print("-"*50)
        print("The current data is: ")
        for student in student_data:
            print(f"{student["FirstName"]}, {student["LastName"]}, {student["CourseName"]}")
        print("-"*50, end="\n\n")


# Processing Layer / Execution block
if __name__ == "__main__":
    students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

    while True:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()
        match menu_choice:
            case "1":
                IO.input_student_data(student_data=students)
            
            case "2":
                IO.output_student_courses(student_data=students)
            
            case "3":
                FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
                print("INFO: Registrations have been saved.")
            
            case "4":
                print("Program Ended.")
                exit()
