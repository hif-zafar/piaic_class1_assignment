def make_shirt(size="large", message="I love TypeScript"):
    """Prints a sentence summarizing the size and message on the shirt."""
    print(f"Size: {size.upper()}, Message: {message}")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="Coding is Not Boring.")
