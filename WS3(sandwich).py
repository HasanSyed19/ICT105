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
sandwich_orders = ["Tuna", "Pastrami", "Club", "BLT", "Pastrami", "Turkey", "Italian", "Pastrami"]
finished_sandwiches = []

# Print message about running out of pastrami and remove pastrami from orders
print("We're out of pastrami!")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

# Loop through sandwich orders and print messages
for sandwich in sandwich_orders:
  print(f"I made your {sandwich.lower()} sandwich!")
  finished_sandwiches.append(sandwich)

# Print finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
