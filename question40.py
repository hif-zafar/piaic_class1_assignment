def make_album(artist, title, tracks=None):
    """Builds a dictionary describing a music album."""
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

# Make three dictionaries representing different albums
album1 = make_album("Ali zafar", "Balaghal-Ula Bi-Kamaalihi")
album2 = make_album("Atif Aslam", "Tajdar-e-Haram", tracks=12)
album3 = make_album("Maher Zain", "Rahmatun Lil'Alameen", tracks=13)

# Print each return value to show the album information
print(album1)
print(album2)
print(album3)
