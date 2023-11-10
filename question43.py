# Exercise 40: Make Album
def make_album(artist, title, tracks=None):
    """Builds a dictionary describing a music album."""
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

# Exercise 43: Unchanged Magicians
def show_magicians(magicians):
    """Prints the name of each magician in the array."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Adds 'the Great' to each magician's name."""
    great_magicians = []  # Create a new array to store the modified names
    for magician in magicians:
        great_magician = f"The Great {magician}"
        great_magicians.append(great_magician)
    return great_magicians  # Return the new array

# Example usage for make_album function
album1 = make_album("Ali Zafar", "Balaghal-Ula Bi-Kamaalihi")
album2 = make_album("Atif Aslam", "Tajdar-e-Haram", tracks=12)
album3 = make_album("Maher Zain", "Rahmatun Lil'Alameen", tracks=13)

# Print each return value to show the album information
print("\nAlbum Information:")
print(album1)
print(album2)
print(album3)

# Original Magicians array
magician_names = ["Harry potter", "Albus Dumbledore", "Hermione", "Ron"]
print("\nOriginal Magicians:")
show_magicians(magician_names)

# Call make_great function with a copy of the array
great_magicians = make_great(magician_names[:])  # Pass a copy of the array
print("\nModified Magicians:")
show_magicians(great_magicians)

# Original array remains unchanged
print("\nOriginal Magicians (Unchanged):")
show_magicians(magician_names)
