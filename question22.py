# List of dictionaries representing countries
countries = [
    {"name": "United States", "capital": "Washington, D.C."},
    {"name": "Canada", "capital": "Ottawa"},
    {"name": "United Kingdom", "capital": "London"},
    {"name": "France", "capital": "Paris" },
    {"name": "Germany", "capital": "Berlin"},
    {"name": "Japan", "capital": "Tokyo"},
    {"name": "Australia", "capital": "Canberra"},
    {"name": "Pakistan", "capital": "Islamabad"},
    {"name": "India", "capital": "New Delhi"},
    {"name": "Turkey", "capital": "Ankara"},
]

# Try to access an index beyond the length of the list (intentional error)
try:
    print(countries[5])  # This index doesn't exist (should produce an IndexError)
except IndexError as e:
    print(f"Intentional Error: {e}")
else:
    # If no error occurs, print information about each country
    print("Information about Countries:")
    for country in countries:
        print(f"- {country['name']}: Capital - {country['capital']}")
