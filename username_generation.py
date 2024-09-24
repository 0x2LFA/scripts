#!/usr/bin/python3
import re

def generate_usernames(name, surname):
    # Remove special characters using regex
    name = re.sub(r"[^\w\s]", "", name)
    surname = re.sub(r"[^\w\s]", "", surname)

    # Create the base variations
    variations = set()
    
    # Capitalized versions
    variations.add(name)                      # Original name
    variations.add(name.lower())             # Lowercase name
    variations.add(surname)                  # Original surname
    variations.add(surname.lower())          # Lowercase surname
    variations.add(surname.capitalize())      # Capitalized surname
    
    # Combined versions
    combined_name = name + surname           # Combined original
    combined_lower = combined_name.lower()   # Combined lowercase
    combined_capitalized = combined_name.capitalize()  # Capitalized combined

    variations.add(combined_name)            # Original combined
    variations.add(combined_lower)           # Lowercase combined
    variations.add(combined_capitalized)     # Capitalized combined

    return variations

def process_file(file_path):
    all_usernames = set()

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into name and surname
            parts = line.strip().split()
            if len(parts) < 2:
                continue  # Skip lines that don't have at least a name and surname
            
            name = " ".join(parts[:-1])  # Join all but last part for name (to handle multi-part names)
            surname = parts[-1]           # Last part is the surname

            usernames = generate_usernames(name, surname)
            all_usernames.update(usernames)

    return all_usernames

# Specify the path to your input file
input_file_path = 'names.txt'  # Change this to your actual file path
usernames = process_file(input_file_path)

# Print the results sorted
for username in sorted(usernames):
    print(username)

