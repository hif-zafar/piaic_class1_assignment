# Make a list of current users
current_users = ["aniya", "lubaba", "fatima", "amara", "aira"]

# Make a list of new users
new_users = ["hadiya", "nawal", "sumbul", "sabiha", "haleema"]

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users to check for uniqueness
for new_user in new_users:
    # Check if the username is already in use (case-insensitive)
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is not available. Please enter a new username.")
    else:
        print(f"Congratulations! {new_user} is available.")
