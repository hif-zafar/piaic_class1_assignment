# Define an array of usernames
usernames = ["aniya", "lubaba", "fatima", "amara", "aira"]

# Loop through the array and print greetings
for username in usernames:
    if username.lower() == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
