# Tests for equality and inequality with strings
string1 = 'apple'
string2 = 'orange'

print(f"Is string1 equal to string2? I predict False.")
print(string1 == string2)

print(f"Is string1 not equal to string2? I predict True.")
print(string1 != string2)

# Tests using the lower case function
string3 = 'ApPle'

print(f"Is string3 in lowercase equal to 'apple'? I predict True.")
print(string3.lower() == 'apple')

# Numerical tests
number1 = 5
number2 = 10

print(f"Is number1 equal to number2? I predict False.")
print(number1 == number2)

print(f"Is number1 not equal to number2? I predict True.")
print(number1 != number2)

print(f"Is number1 greater than number2? I predict False.")
print(number1 > number2)

print(f"Is number1 less than number2? I predict True.")
print(number1 < number2)

print(f"Is number1 greater than or equal to number2? I predict False.")
print(number1 >= number2)

print(f"Is number1 less than or equal to number2? I predict True.")
print(number1 <= number2)

# Tests using "and" and "or" operators
print(f"Is number1 less than number2 and number1 + number2 equal to 15? I predict True.")
print(number1 < number2 and number1 + number2 == 15)

print(f"Is number1 less than number2 or number1 + number2 equal to 14? I predict True.")
print(number1 < number2 or number1 + number2 == 14)

# Test whether an item is in an array
array1 = [1, 2, 3, 4, 5]
item_to_check = 3

print(f"Is item_to_check in array1? I predict True.")
print(item_to_check in array1)

# Test whether an item is not in an array
item_not_in_array = 6

print(f"Is item_not_in_array not in array1? I predict True.")
print(item_not_in_array not in array1)
