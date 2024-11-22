# Reverse a String

## Project Overview
This project is a simple yet foundational exercise designed to help learners get started with Python while introducing basic concepts of string manipulation. The goal is to implement a function that takes a string as input and returns its reversed version. This exercise serves as a stepping stone toward mastering data structures and algorithms.

---

## Why This Project?
Reversing a string is an excellent way to:
- Understand the concept of **slicing** in Python.
- Learn about **iteration** and **looping** as alternative solutions.
- Gain confidence in writing and testing simple functions.
- Explore the importance of **efficiency** and the versatility of Python's built-in features.

---

## How It Works
The project involves:
1. Writing a function `reverse_string` that uses **slicing** to reverse a string efficiently.
2. Including an alternative implementation that uses a **loop** to manually reverse a string.
3. Using a `__name__ == "__main__"` block to test the function interactively.

### Input
A string provided by the user.

### Output
The reversed version of the input string.

---

## Code
Here's the main implementation:

```python
def reverse_string(stringreverse):
    """
    Function takes a string as input and returns its reversed version.
    """
    reversed_string = stringreverse[::-1]  # Slice the string to reverse it
    return reversed_string  # Return the reversed string

if __name__ == "__main__":
    userinput = input("Enter the string here: \n")  # Get user input
    result = reverse_string(userinput)  # Call the function with the input
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


## Example Run
```plaintext
Enter the string here:
hello
The reversed string is: olleh
