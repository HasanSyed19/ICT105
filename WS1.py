# Variable Declaration and Types
a = 15
b = 12

# Print the types for a and b
print("Type of a:", type(a))
print("Type of b:", type(b))
# Basic Arithmetic Operations
# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)
a = 10
b = 3

# Integer division with type casting
c = int(a / b)  # c will be 3 (integer part of the division)

print("Value of c (integer):", c)
print("Type of c:", type(c))

# Convert c to float and print its new value and type
c_float = float(c)  # Convert integer c to float

print("\nValue of c (float):", c_float)
print("Type of c (float):", type(c_float))
a = 10
b = 3

# Integer division with type casting
c = int(a / b)  # c will be 3 (integer part of the division)

# Create a message string
message = "The result of a divided by b is: "

# Convert c to string and concatenate with message
message_with_result = message + str(c)

print(message_with_result)
a = 10
b = 3

# Comparison using greater than operator
is_a_greater_than_b = a > b
print("Is a greater than b:", is_a_greater_than_b)  # Output: True

# Comparison using equal to operator
is_a_equal_to_b = a == b
print("Is a equal to b:", is_a_equal_to_b)  # Output: False
a = 10
b = 3

# Integer division with type casting
c = int(a / b)  # c will be 3 (integer part of the division)

# Create a message string
message = "The result of a divided by b is: "

# Convert c to string and concatenate with message
message_with_result = message + str(c)

# Print results on separate lines with clear labels

print("Value of c (integer):", c)
print("Type of c:", type(c))

print("\nValue of c (float):", float(c))  # Convert and print directly
print("Type of c (float):", type(float(c)))

print("\nIs a greater than b:", a > b)  # Compare and print directly
print("Is a equal to b:", a == b)  # Compare and print directly

