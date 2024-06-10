# Save content to the file
with open('learning_python.txt', 'w') as file:
    file.write("Learning Python is fun and rewarding.\n")
    file.write("You can build web applications, automate tasks, and analyze data.\n")
    file.write("Python has a simple syntax and a vast ecosystem of libraries.\n")

# Read and print the entire file content at once
with open('learning_python.txt', 'r') as file:
    content = file.read()
    print("Printing the entire file content at once:\n")
    print(content)

# Read the file and store lines in a list, then loop over each line to print
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    print("Printing the file content line by line:\n")
    for line in lines:
        print(line, end='')  # end='' to avoid adding extra new lines
# Write content to the file
with open('learning_python.txt', 'w') as file:
    file.write("Learning Python is fun and rewarding.\n")
    file.write("You can build web applications, automate tasks, and analyze data.\n")
    file.write("Python has a simple syntax and a vast ecosystem of libraries.\n")

# Read the file and replace 'Python' with 'C', then print each modified line
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        modified_line = line.replace('Python', 'C')
        print(modified_line, end='')  # end='' to avoid adding extra new lines
def add_two_numbers():
    try:
        # Prompt for the first number
        num1 = input("Enter the first number: ")
        # Convert the input to an integer
        num1 = int(num1)
        
        # Prompt for the second number
        num2 = input("Enter the second number: ")
        # Convert the input to an integer
        num2 = int(num2)
        
        # Add the two numbers
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}.")
    
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Error: Please enter valid numbers.")

# Test the function
add_two_numbers()
def add_two_numbers():
    while True:
        try:
            # Prompt for the first number
            num1 = input("Enter the first number (or 'q' to quit): ")
            if num1.lower() == 'q':
                print("Exiting the program. Goodbye!")
                break
            num1 = int(num1)
            
            # Prompt for the second number
            num2 = input("Enter the second number (or 'q' to quit): ")
            if num2.lower() == 'q':
                print("Exiting the program. Goodbye!")
                break
            num2 = int(num2)
            
            # Add the two numbers
            result = num1 + num2
            print(f"The result of adding {num1} and {num2} is {result}.\n")
        
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Error: Please enter valid numbers.\n")

# Run the addition calculator
add_two_numbers()
