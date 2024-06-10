def make_shirt(size, text):
  """Prints a summary of the shirt order"""
  print("\nYou've ordered a " + size + " shirt that says \"" + text + "\"")

# Part 1: Positional arguments
make_shirt('large', "I love Python!")  # Passing size and text as positional arguments

# Part 2: Keyword arguments
make_shirt(size='medium', text="Readability counts")  # Using keyword arguments
def make_shirt(size="large", text="I love Python!"):
  """Prints a summary of the shirt order"""
  print("\nYou've ordered a " + size + " shirt that says \"" + text + "\"")

# Part 1: Large shirt with default message
make_shirt()  # No arguments passed, uses default values

# Part 2: Medium shirt with default message
make_shirt(size="medium")  # Specify only size

# Part 3: Small shirt with a different message
make_shirt(size="small", text="Python is fun!")  # Specify both size and text
def describe_city(city, country="USA"):
  """Prints a sentence about a city being in a country"""
  print(city.title() + " is located in " + country.title() + ".")

# Call the function for three cities
describe_city("tokyo", "japan")
describe_city("berlin")
describe_city("são paulo", "brazil")
def make_sandwich(*items):
  """Prints a summary of the sandwich order"""
  print("\nI'm making a sandwich with:")
  for item in items:
    print("-", item.title())

# Call the function with three different numbers of arguments
make_sandwich("bread", "cheese", "turkey")
make_sandwich("roast beef", "mustard")
make_sandwich("hummus", "spinach", "tomato")
def build_profile(first, last, **other_info):
  """Builds a dictionary containing user information"""
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  for key, value in other_info.items():
    profile[key] = value
  return profile

my_profile = build_profile('Bard', 'Large language model', 
  field='Computer Science', 
  favorite_hobby='Learning new things')

print(my_profile)
def make_car(manufacturer, model, **other_info):
  """Creates a dictionary storing car information"""
  car_info = {}
  car_info['manufacturer'] = manufacturer
  car_info['model'] = model
  for key, value in other_info.items():
    car_info[key.lower()] = value  # Convert keys to lowercase for consistency
  return car_info

# Example usage
my_car = make_car('subaru', 'outback', color='blue', year=2022)
print(my_car)
def make_car(manufacturer, model, **other_info):
  """Creates a dictionary storing car information"""
  car_info = {}
  car_info['manufacturer'] = manufacturer
  car_info['model'] = model
  for key, value in other_info.items():
    car_info[key.lower()] = value  # Convert keys to lowercase
  return car_info

# Call the function with required information and two other arguments
my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)
