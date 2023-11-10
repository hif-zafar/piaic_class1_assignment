# Exercise 39: City Names
def city_country(city, country):
    """Returns a formatted string with the city and its country."""
    return f"{city}, {country}"

# Exercise 42: Great Magicians
def show_magicians(magicians):
    """Prints the name of each magician in the array."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Adds 'the Great' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] = f"The Great {magicians[i]}"

# Example usage for city_country function
result1 = city_country("Lahore", "Pakistan")
result2 = city_country("Paris", "France")
result3 = city_country("Tokyo", "Japan")

# Print the returned values for city_country
print(result1)
print(result2)
print(result3)

# Example usage for make_great function
magician_names = ["Harry potter", "Albus Dumbledore", "Hermione", "Ron"]
print("\nOriginal Magicians:")
show_magicians(magician_names)

make_great(magician_names)
print("\nModified Magicians:")
show_magicians(magician_names)
