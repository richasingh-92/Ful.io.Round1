import re

def is_valid_contact_number(contact_number):
    # Regular expression pattern for valid contact numbers
    pattern = r'^(\+?\d{0,2}\s?)?[-.\s]?(\(\d{1,3}\)|\d{1,3})[-.\s]?\d{1,3}[-.\s]?\d{4}$'

    # Check if the input matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False

contact_numbers = input("Enter contact number: ")

if is_valid_contact_number(contact_numbers):
    print(f"{contact_numbers} is a valid contact number.")
else:
    print(f"{contact_numbers} is an invalid contact number.")