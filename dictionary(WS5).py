import json

def collect_user_info():
    """Collect information about the user."""
    user_info = {}
    user_info['name'] = input("Enter your name: ")
    user_info['age'] = input("Enter your age: ")
    user_info['favorite_color'] = input("Enter your favorite color: ")
    return user_info

def store_user_info(user_info):
    """Store user information in a file."""
    filename = 'user_info.json'
    with open(filename, 'w') as file:
        json.dump(user_info, file)
    print("Your information has been stored.")

def read_user_info():
    """Read user information from a file."""
    filename = 'user_info.json'
    try:
        with open(filename, 'r') as file:
            user_info = json.load(file)
        return user_info
    except FileNotFoundError:
        return None

def print_user_summary(user_info):
    """Print a summary of the user information."""
    if user_info:
        print("\nHere's what I remember about you:")
        for key, value in user_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No user information found.")

def main():
    """Main function to execute the program."""
    user_info = read_user_info()
    if user_info:
        print_user_summary(user_info)
    else:
        user_info = collect_user_info()
        store_user_info(user_info)
        print_user_summary(user_info)

# Run the main function to execute the program
main()
