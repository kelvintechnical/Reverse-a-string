def reverse_string(stringreverse):
    '''
    Function takes a string as input and will reverse the string.
    '''
    reversed_string = stringreverse[::-1]  # Slice the string to reverse it
    return reversed_string  # Correct variable name

if __name__ == "__main__":
    userinput = input("Enter the string here: \n")  # Get user input
    result = reverse_string(userinput)  # Call the function
    print(f"The reversed string is: {result}")  # Print the result

    '''
    Explanation of __name__ == "__main__"
    if __name__ == "__main__":
    - This block ensures that the code inside it only runs when the file is executed directly.
    - If the file is imported as a module in another script, the code inside this block won't execute.
    
    Why use __name__ == "__main__"?
    - It allows your script to serve a dual purpose:
      1. As a standalone program: Runs the code inside the if block when executed.
      2. As a module: Lets other programs import your function reverse_string without executing the test code.
    '''
