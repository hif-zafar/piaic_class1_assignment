# Original guest list
guest_list = ["Aisha", "usama", "tayyab", "Imran", "muawiya", "Zainab"]

# Print invitations to each person
for guest in guest_list:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner. It would be an honor to have you join us!\nSincerely, [HifzaZafar]")

# Inform about the bigger dinner table
print("\nGreat news! We found a bigger dinner table!\n")

# Add new guests to the list
new_guests = ["Ali", "Sara"]
guest_list.insert(0, new_guests[0])  # Add to the beginning of the list
guest_list.insert(len(guest_list) // 2, new_guests[1])  # Add to the middle of the list
guest_list.append("Ahmed")  # Add to the end of the list

# Print invitations to each person
for guest in guest_list:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner. It would be an honor to have you join us!\nSincerely, [HifzaZafar]")

# Inform that only two people can be invited
print("\nUnfortunately, the new dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Remove guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, we can't invite you to dinner.")

# Print a message to the remaining two guests
for remaining_guest in guest_list:
    print(f"Dear {remaining_guest},\n\tYou're still invited to dinner. We look forward to seeing you!\nSincerely, [HifzaZafar]")

# Print the number of people invited to dinner
print(f"\nNumber of people invited to dinner: {len(guest_list)}")
