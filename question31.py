# Define an array of usernames
usernames = []

# Check if the list of users is not empty
if usernames:
    # Loop through the array and print greetings
    for username in usernames:
        if username.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    # Print a message if the list is empty
    print("We need to find some users!")
