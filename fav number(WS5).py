import json

def store_favorite_number():
    favorite_number = input("Enter your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
    print(f"Your favorite number {favorite_number} has been stored.")

# Run the function to store the favorite number
store_favorite_number()
import json

def read_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename, 'r') as file:
            favorite_number = json.load(file)
        print(f"I know your favorite number! It's {favorite_number}.")
    except FileNotFoundError:
        print("The favorite number file does not exist.")

# Run the function to read and print the favorite number
read_favorite_number()
import json

def get_stored_favorite_number():
    """Get stored favorite number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename, 'r') as file:
            favorite_number = json.load(file)
        return favorite_number
    except FileNotFoundError:
        return None

def store_favorite_number():
    """Prompt for a new favorite number and store it."""
    favorite_number = input("Enter your favorite number: ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
    print(f"Your favorite number {favorite_number} has been stored.")

def report_favorite_number():
    """Report the stored favorite number to the user."""
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        store_favorite_number()

# Run the function to report the favorite number or store it if not found
report_favorite_number()
