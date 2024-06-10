# Global destinations to explore (not alphabetical order)
destinations = ["Iceland", "Japan", "Peru", "Morocco", "New Zealand"]

# Print the original list (raw Python list)
print("Original List:", destinations)

# Print the list in alphabetical order (without modifying the original list)
print("\nAlphabetical Order (sorted()):", sorted(destinations))

# Print the original list again (to show it's unchanged)
print("\nOriginal List (unchanged):", destinations)

# Print the list in reverse alphabetical order (without modifying the original list)
print("\nReverse Alphabetical Order (sorted()):", sorted(destinations, reverse=True))

# Print the original list again (to show it's unchanged)
print("\nOriginal List (unchanged):", destinations)

# Reverse the order of the list
destinations.reverse()
print("\nList Reversed (using reverse()):", destinations)

# Reverse the order of the list again (back to original)
destinations.reverse()
print("\nList Back to Original Order (using reverse()):", destinations)

# Sort the list alphabetically (modifying the original list)
destinations.sort()
print("\nList Sorted Alphabetically (using sort()):", destinations)

# Sort the list in reverse alphabetical order (modifying the original list)
destinations.sort(reverse=True)
print("\nList Sorted Reverse Alphabetically (using sort()):", destinations)
# Guest list
guests = ["Alice", "Bob", "Charlie"]

# Print invitations
for guest in guests:
  print(f"Dear {guest}, you are invited to dinner!")
# Guest list
guests = ["Alice", "Bob", "Charlie"]

# Print initial invitations
for guest in guests:
  print(f"Dear {guest}, you are invited to dinner!")

# A guest can't make it, so update the list
print("\nUh oh, someone can't make it!")
guests.remove("Charlie")  # Replace "Charlie" with the actual name
guests.append("David")  # Add the new guest's name

# Print new invitations
print("\nSending out new invitations:")
for guest in guests:
  print(f"Dear {guest}, you are still invited to dinner!")
# Guest list
guests = ["Alice", "Bob", "Charlie"]

# Print initial invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# A guest can't make it, so update the list
print("\nUh oh, someone can't make it!")
guests.remove("Charlie")  # Replace "Charlie" with the actual name
guests.append("David")  # Add the new guest's name

# Print new invitations
print("\nSending out new invitations:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")

# Bigger table available, add more guests!
print("\nGreat news! We found a bigger table!")

# Add a guest at the beginning
guests.insert(0, "Emily")

# Add a guest in the middle (index 2 here, adjust for list length)
guests.insert(2, "Fred")

# Add a guest at the end
guests.append("Grace")

# Print invitations for the final list
print("\nNew invitations for everyone:")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner! We have a bigger table now.")
# Guest list
guests = ["Alice", "Bob", "Charlie", "David", "Emily", "Fred", "Grace"]

# Print invitations for the initial list
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# A guest can't make it, so update the list
print("\nUh oh, someone can't make it!")
guests.remove("Charlie")  # Replace "Charlie" with the name who can't make it
guests.append("David")  # Add the new guest's name

# Print invitations for the updated list
print("\nSending out new invitations:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")

# Bigger table available, then table won't arrive on time (limited space)
print("\nGreat news! We found a bigger table... oh no, it won't arrive on time!")
print("We can only invite two people for dinner. So sorry to some of you!")

# Remove guests until only two remain
number_to_remove = len(guests) - 2
for i in range(number_to_remove):
    guest_to_remove = guests.pop()  # Remove and store the guest's name
    print(f"\nSorry, {guest_to_remove}, but due to space limitations, I cannot invite you to dinner this time.")

# Print invitations for the remaining guests
print("\nThe remaining invitations:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")
age = 30  # Set a value for age (you can change this value)

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
usernames = ["alice123", "bob_the_builder", "charlie45", "admin", "guest_user"]

# Loop through usernames
for username in usernames:
    if username == "admin":
        print(f"Hello Admin. Would you like to see a status report?")
    else:
        print(f"Hello, {username}, thank you for logging in again.")
