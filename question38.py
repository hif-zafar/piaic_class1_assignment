def describe_city(city, country="Pakistan"):
    """Prints a simple sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Karachi")
describe_city("Paris", "France")
describe_city("Tokyo", "Japan")
