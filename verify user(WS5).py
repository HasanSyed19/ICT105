import json
from pathlib import Path

def get_stored_username():
    """Get stored username if available."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None

def store_username(username):
    """Store the username in a file."""
    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        current_username = input(f"Is your name {username}? (yes/no) ").strip().lower()
        if current_username == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = input("What is your name? ").strip()
            store_username(username)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = input("What is your name? ").strip()
        store_username(username)
        print(f"We'll remember you when you come back, {username}!")

# Run the greet_user function to execute the program
greet_user()
