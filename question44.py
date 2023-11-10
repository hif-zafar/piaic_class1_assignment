def make_sandwich(*items):
    """Prints a summary of the sandwich being ordered."""
    print("\nSandwich Summary:")
    if items:
        print("You ordered a sandwich with the following items:")
        for item in items:
            print(f"- {item}")
    else:
        print("You ordered an empty sandwich. Please add some items!")

# Call the function three times with a different number of arguments
make_sandwich("Turkey", "Swiss Cheese", "korean", "Tomato", "Mayo")
make_sandwich("Ham", "Cheddar Cheese", "Mustard")
make_sandwich("Veggie Patty", "Pepper Cheese", "Spinach", "Onion", "Chilli Sauce")
