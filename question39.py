def city_country(city, country):
    """Returns a formatted string with the city and its country."""
    return f"{city}, {country}"

# Call the function with three city-country pairs
result1 = city_country("Lahore", "Pakistan")
result2 = city_country("Paris", "France")
result3 = city_country("Tokyo", "Japan")

# Print the returned values
print(result1)
print(result2)
print(result3)
