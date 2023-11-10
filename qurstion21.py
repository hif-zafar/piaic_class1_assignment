# List of dictionaries representing countries
countries = [
    {"name": "United States", "capital": "Washington, D.C."},
    {"name": "Canada", "capital": "Ottawa"},
    {"name": "United Kingdom", "capital": "London"},
    {"name": "France", "capital": "Paris"},
    {"name": "Germany", "capital": "Berlin" },
    {"name": "Japan", "capital": "Tokyo"},
    {"name": "Australia", "capital": "Canberra"},
    {"name": "Pakistan", "capital": "Islamabad"},
    {"name": "India", "capital": "New Delhi"},
    {"name": "Turkey", "capital": "Ankara" },
]

# Print information about each country
print("Information about Countries:")
for country in countries:
    print(f"- {country['name']}: Capital - {country['capital']}")
