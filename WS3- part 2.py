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


