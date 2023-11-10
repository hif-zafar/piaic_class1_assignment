# Original guest list
guest_list = ["usama", "tayyab", "hunzala", "muawiya"]

# Print invitations to each person
for guest in guest_list:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner. It would be an honor to have you join us!\nSincerely, [Your Name]")

# Identify a guest who can't make it
guest_cant_make_it = "hunzala"

# Print a message about the guest who can't make it
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = "Imran"
guest_list[guest_list.index(guest_cant_make_it)] = new_guest

# Print second set of invitations to each person
for guest in guest_list:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner. It would be an honor to have you join us!\nSincerely, [hifzazafar]")

# Inform about the bigger dinner table
print("\nGreat news! We found a bigger dinner table!\n")

# Add new guests to the list
new_guests = ["Aisha", "Ali"]
guest_list.insert(0, new_guests[0])  # Add to the beginning of the list
guest_list.insert(len(guest_list) // 2, new_guests[1])  # Add to the middle of the list
guest_list.append("Zainab")  # Add to the end of the list

# Print third set of invitations to each person
for guest in guest_list:
    print(f"Dear {guest},\n\tYou are cordially invited to dinner. It would be an honor to have you join us!\nSincerely, [hifzazafar]")
