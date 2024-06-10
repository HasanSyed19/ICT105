# Person dictionaries
person1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Software Engineer"
}

person2 = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles",
    "occupation": "Musician"
}

# List of people
people = [person1, person2]

# Print information about each person
for person in people:
  print("-" * 30)  # Separator for better readability
  for key, value in person.items():
    print(f"{key.title()}: {value}")  # Title case for keys and print values
# Pet dictionaries
pet1 = {
    "kind": "Cat",
    "owner": "Alice"
}

pet2 = {
    "kind": "Dog",
    "owner": "Bob"
}

pet3 = {
    "kind": "Fish",
    "owner": "Charlie"
}

# List of pets
pets = [pet1, pet2, pet3]

# Print information about each pet
for pet in pets:
  print("-" * 30)  # Separator for readability
  for key, value in pet.items():
    print(f"{key.title()}: {value}")
# Favorite places dictionary
favorite_places = {
    "Alice": ["Paris, France", "New York City, USA"],
    "Bob": ["Tokyo, Japan", "Mount Fuji, Japan"],
    "Charlie": ["The Great Barrier Reef, Australia"]
}

# Print favorite places
for name, places in favorite_places.items():
    print(f"{name}'s favorite places:")
    if len(places) > 1:  # Check if there are multiple places
        for place in places:
            print(f"- {place}")  # Print each place on a new line
    else:
        print(f"- {places[0]}")  # Print the single place if there's only one
# Favorite numbers dictionary
favorite_numbers = {
    "Alice": [7, 22],
    "Bob": [3, 14, 15],
    "Charlie": [108]  # Charlie has only one favorite number
}

# Print favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite number(s):")
    if len(numbers) > 1:  # Check if there are multiple numbers
        for number in numbers:
            print(f"- {number}")  # Print each number on a new line
    else:
        print(f"- {numbers[0]}")  # Print the single number if there's only one
cities = {
  "Tokyo": {
    "country": "Japan",
    "population": "37.4 million",
    "fact": "Tokyo is the most populous metropolitan area in the world."
  },
  "Paris": {
    "country": "France",
    "population": "2.1 million",
    "fact": "Paris is known as the 'City of Lights' for its romantic atmosphere."
  },
  "New York City": {
    "country": "United States",
    "population": "8.4 million",
    "fact": "New York City is a global center for finance, media, culture, and fashion."
  }
}

for city, info in cities.items():
  print(f"\n{city.title()}:")
  for key, value in info.items():
    print(f"\t{key.title()}: {value}")
toppings = []

while True:
  topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()
  if topping == 'quit':
    break
  else:
    toppings.append(topping)
    print(f"Adding {topping} to your pizza!")

if toppings:
  print("\nYour pizza toppings:")
  for topping in toppings:
    print(f"- {topping}")
else:
  print("You didn't choose any toppings.")
while True:
  age = input("What is your age?: ")
  if not age.isdigit():  # Check if input is a digit (number)
    print("Please enter a number for your age.")
  elif int(age) < 0:
    print("Age cannot be negative.")
  else:
    # Valid age entered, break the loop and process it
    break  

# Process the age obtained (e.g., calculate ticket price)
if int(age) < 3:
  print("YOU ARE FREE!")
elif int(age) < 13:
  print("YOU ARE $10.00")
else:
  print("YOU ARE $15.00")
active = True
while active:
  age = input("What is your age?: ")
  if not age.isdigit():
    print("Please enter a number for your age.")
  elif int(age) < 0:
    print("Age cannot be negative.")
  else:
    # Valid age entered, potentially process it or ask if user wants to continue
    if input("Do you want to enter another age (y/n)?: ").lower() != 'y':
      active = False  # Set active to False to exit the loop

# Process the final age obtained (if needed)
if int(age) < 3:
  print("YOU ARE FREE!")
elif int(age) < 13:
  print("YOU ARE $10.00")
else:
  print("YOU ARE $15.00")
while True:
  age = input("What is your age?: ")
  if not age.isdigit():
    print("Please enter a number for your age.")
  elif int(age) < 0:
    print("Age cannot be negative.")
  elif age.lower() == 'quit':
    break  # Exit the loop if user enters 'quit'
  else:
    # Valid age entered, process it
    if int(age) < 3:
      print("YOU ARE FREE!")
    elif int(age) < 13:
      print("YOU ARE $10.00")
    else:
      print("YOU ARE $15.00")

# No further processing needed after exiting the loop
while True:
  print("This loop will continue indefinitely...")
sandwich_orders = ["Tuna", "Club", "BLT", "Grilled Cheese"]
finished_sandwiches = []

# Loop through sandwich orders and print messages
for sandwich in sandwich_orders:
  print(f"I made your {sandwich.lower()} sandwich!")
  finished_sandwiches.append(sandwich)

# Print finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")

