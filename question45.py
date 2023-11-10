def car_info(manufacturer, model, **kwargs):
    """Stores information about a car in a dictionary."""
    car = {"Manufacturer": manufacturer, "Model": model}
    car.update(kwargs)
    return car

# Call the function with required information and additional key-value pairs
car_details = car_info("Toyota", "Camry", color="Blue", year=2022, optional_feature="Sunroof")

# Print the dictionary (Object) returned by the function
print("Car Information:")
print(car_details)
