class User:
  """A class representing a user profile."""

  def __init__(self, first_name, last_name, email, age, location):
    """Initialize the user's attributes."""
    self.first_name = first_name.title()  # Store name with first letter capitalized
    self.last_name = last_name.title()
    self.email = email
    self.age = age
    self.location = location.title()

  def describe_user(self):
    """Print a summary of the user's information."""
    print(f"\n{self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}. Their email is {self.email.lower()}.")

  def greet_user(self):
    """Print a personalized greeting to the user."""
    print(f"\nHello, {self.first_name}! Welcome.")

# Create several user instances
user1 = User('eric', 'matthes', 'eric.matthes@gmail.com', 34, 'new york')
user2 = User('ada', 'lovelace', 'ada.lovelace@example.com', 197, 'london')
user3 = User('marie', 'curie', 'marie.curie@science.com', 66, 'paris')

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
class User:
  """A class representing a user profile."""

  def __init__(self, first_name, last_name, email, age, location):
    """Initialize the user's attributes."""
    self.first_name = first_name.title()
    self.last_name = last_name.title()
    self.email = email
    self.age = age
    self.location = location.title()
    self.login_attempts = 0  # Initialize login attempts to 0

  def describe_user(self):
    """Print a summary of the user's information."""
    print(f"\n{self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}. Their email is {self.email.lower()}.")

  def greet_user(self):
    """Print a personalized greeting to the user."""
    print(f"\nHello, {self.first_name}! Welcome.")

  def increment_login_attempts(self):
    """Increment the number of login attempts by 1."""
    self.login_attempts += 1

  def reset_login_attempts(self):
    """Reset the number of login attempts to 0."""
    self.login_attempts = 0

# Create a user instance
user = User('eric', 'matthes', 'eric.matthes@gmail.com', 34, 'new york')

# Try to login a few times
print(f"\nLogin attempts: {user.login_attempts}")  # Print initial attempts (0)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after incrementing: {user.login_attempts}")  # Print attempts after incrementing

# Reset login attempts
user.reset_login_attempts()
print(f"Login attempts after resetting: {user.login_attempts}")  # Print attempts after resetting
class Restaurant:
  """A class representing a restaurant."""

  def __init__(self, restaurant_name, cuisine_type):
    """Initialize the restaurant's attributes."""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    """Print a summary of the restaurant's information."""
    print(f"\nRestaurant name: {self.restaurant_name}")
    print(f"Cuisine type: {self.cuisine_type}")

  def open_restaurant(self):
    """Print a message indicating the restaurant is open."""
    print(f"{self.restaurant_name} is now open!")

# Create a restaurant instance
restaurant = Restaurant('The Curry House', 'Indian')

# Print attributes individually
print(f"\nRestaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call describe_restaurant()
restaurant.describe_restaurant()

# Call open_restaurant()
restaurant.open_restaurant()

# Create three more restaurant instances
italian_restaurant = Restaurant("La Cucina", "Italian")
french_restaurant = Restaurant("Le Bistro", "French")
japanese_restaurant = Restaurant("Sushi Paradise", "Japanese")

# Call describe_restaurant() for each instance
italian_restaurant.describe_restaurant()
french_restaurant.describe_restaurant()
japanese_restaurant.describe_restaurant()
class Restaurant:
  """A class representing a restaurant."""

  def __init__(self, restaurant_name, cuisine_type):
    """Initialize the restaurant's attributes."""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0  # Initialize number served to 0

  def describe_restaurant(self):
    """Print a summary of the restaurant's information."""
    print(f"\nRestaurant name: {self.restaurant_name}")
    print(f"Cuisine type: {self.cuisine_type}")
    print(f"Customers served: {self.number_served}")

  def open_restaurant(self):
    """Print a message indicating the restaurant is open."""
    print(f"{self.restaurant_name} is now open!")

  def set_number_served(self, new_number):
    """Set the number of customers that have been served."""
    self.number_served = new_number

  def increment_number_served(self, number_to_increment):
    """Increment the number of customers served."""
    self.number_served += number_to_increment

# Create a restaurant instance
restaurant = Restaurant('The Curry House', 'Indian')

# Print initial number served
print(f"\nCustomers served: {restaurant.number_served}")

# Change the value and print again
restaurant.number_served = 50
print(f"Customers served after change: {restaurant.number_served}")

# Set the number served with a method call
restaurant.set_number_served(100)
print(f"Customers served after set_number_served(): {restaurant.number_served}")

# Increment the number served for a day's business
restaurant.increment_number_served(75)
print(f"Customers served after increment_number_served(): {restaurant.number_served}")
class Restaurant:
  """A class representing a restaurant."""

  def __init__(self, restaurant_name, cuisine_type):
    """Initialize the restaurant's attributes."""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    """Print a summary of the restaurant's information."""
    print(f"\nRestaurant name: {self.restaurant_name}")
    print(f"Cuisine type: {self.cuisine_type}")
    print(f"Customers served: {self.number_served}")

  def open_restaurant(self):
    """Print a message indicating the restaurant is open."""
    print(f"{self.restaurant_name} is now open!")

  def set_number_served(self, new_number):
    """Set the number of customers that have been served."""
    self.number_served = new_number

  def increment_number_served(self, number_to_increment):
    """Increment the number of customers served."""
    self.number_served += number_to_increment


class IceCreamStand(Restaurant):
  """A class representing an ice cream stand."""

  def __init__(self, restaurant_name, cuisine_type="ice cream"):
    """Initialize the ice cream stand's attributes (inherits from Restaurant)."""
    super().__init__(restaurant_name, cuisine_type)  # Call parent class constructor
    self.flavors = []  # Initialize empty list for flavors

  def display_flavors(self):
    """Print a list of available ice cream flavors."""
    print(f"\nIce cream flavors at {self.restaurant_name}:")
    for flavor in self.flavors:
      print(f"- {flavor}")

# Create an ice cream stand instance
ice_cream_stand = IceCreamStand("Cool Cones")

# Add some flavors
ice_cream_stand.flavors = ["chocolate", "strawberry", "mint chip"]

# Display the flavors
ice_cream_stand.display_flavors()
