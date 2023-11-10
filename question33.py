# Store the numbers 1 through 9 in an array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the array
for number in numbers:
    # Use an if-else chain to print the proper ordinal ending
    if number == 1:
        ordinal = "st"
    elif number == 2:
        ordinal = "nd"
    elif number == 3:
        ordinal = "rd"
    else:
        ordinal = "th"

    # Print the result
    print(f"{number}{ordinal}")
