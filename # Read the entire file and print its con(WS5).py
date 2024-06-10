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
