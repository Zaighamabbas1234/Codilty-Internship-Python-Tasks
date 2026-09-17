# Problem Statement:
# Build a simple calculator.

# Description:
# Create a command-line calculator in Python that supports addition, subtraction, multiplication and division. Include error handling for invalid inputs and division by zero.

# Solution:
# A simple calculator performs basic arithmetic operations like addition, subtraction, multiplication and division.

# Command_Line Simple Python Calculator:
# This version of the calculator runs in the terminal.
# It takes user input, allows the user to select an operation and displays the result.

# Command_Line Simple Python Calculator Code:

# Define a function in Python by using the name calculator:
def calculator():
    print("Command-Line Simple Python Calculator.") # Display the title.
    print("Operations:") # Display the heading.
    print(" + : Addition") # Informing the user that the (+) symbol performs addition.
    print(" - : Subtraction") # Informing the user that the (-) symbol performs subtraction.
    print(" * : Multiplication") # Informing the user that the (*) symbol performs Multiplication.
    print(" / : Division") # Informing the user that the (/) symbol performs division.

# The try statement is used to test a block of code for errors. If an error occurs (such as entering text instead of a number). Python transfers control to the except block instead of stopping the program:
    
    try:
        # Get the user input:
        first_number = float(input("Enter the first number:")) # Prompts the user to enter the first number.
        operator = input("Enter an operator (+,-,*,/):") # Prompts the user to enter the operator.
        second_number = float(input("Enter the second number:")) # Prompts the user to enter the second number.

        # Perform basic calculation: This section of the program uses an if-elif-else conditional statement to determine which arithmetic operation the user selected:
        
        if operator == "+":
            result = first_number+second_number
        elif operator == "-":
            result = first_number-second_number
        elif operator == "*":
            result = first_number*second_number
        elif operator == "/":
            if second_number == 0: # Error handling for invalid division by zero.
                print("Error: Division by zero is not allowed.") 
                return
            result = first_number/second_number
        else:
            print("Error: Invalid operator.") # Error handling for invalid operator.
            return # Stops the function to prevent further execution.
        print(f"Result: {first_number} {operator} {second_number} = {result}") # Shows the output.
        
    except ValueError: # Error handling for invalid inputs.
        print("Error: Please enter valid numeric values.")
        
# Run the calculator:

calculator() # Returns the function.

# Submitted By: Zaigham Abbas.
# Submitted to: HR Codility.
# Dated: 08/06/2026.