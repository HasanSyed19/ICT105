# Create cats.txt and write cat names
with open('cats.txt', 'w') as file:
    file.write("Whiskers\n")
    file.write("Shadow\n")
    file.write("Mittens\n")

# Create dogs.txt and write dog names
with open('dogs.txt', 'w') as file:
    file.write("Buddy\n")
    file.write("Bella\n")
    file.write("Max\n")

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"Contents of {filename}:\n{contents}")
    except FileNotFoundError:
        pass  # Fail silently

# Read and print contents of cats.txt
read_and_print_file('cats.txt')

# Read and print contents of dogs.txt
read_and_print_file('dogs.txt')
