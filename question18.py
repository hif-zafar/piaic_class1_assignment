# Places to visit array
places_to_visit = ["Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad"]

# Print array in its original order
print("Original Order:", places_to_visit)

# Print array in alphabetical order without modifying the original list
print("Alphabetical Order:", sorted(places_to_visit))

# Show that the array is still in its original order
print("Original Order (Still):", places_to_visit)

# Print array in reverse alphabetical order without changing the original list
print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))

# Show that the array is still in its original order
print("Original Order (Still):", places_to_visit)

# Reverse the order of the list
places_to_visit.reverse()

# Print the array to show that its order has changed
print("Reversed Order:", places_to_visit)

# Reverse the order of the list again
places_to_visit.reverse()

# Print the list to show it’s back to its original order
print("Original Order (After Second Reverse):", places_to_visit)

# Sort the array in alphabetical order
places_to_visit.sort()

# Print the array to show that its order has been changed
print("Sorted in Alphabetical Order:", places_to_visit)

# Sort the array in reverse alphabetical order
places_to_visit.sort(reverse=True)

# Print the array to show that its order has been changed
print("Sorted in Reverse Alphabetical Order:", places_to_visit)
