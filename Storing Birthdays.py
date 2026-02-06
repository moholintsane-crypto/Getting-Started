import json

# Load existing birthdays or create new dictionary
def load_birthdays(filename='birthdays.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save birthdays to a JSON file
def save_birthdays(birthdays, filename='birthdays.json'):
    with open(filename, 'w') as f:
        json.dump(birthdays, f)

# Function to add a birthday
def add_birthday(birthdays, name, date):
    birthdays[name] = date
    save_birthdays(birthdays)
    print(f"Added {name}'s birthday: {date}")

# --- Main Application Logic ---
birthdays = load_birthdays()

# Example: Adding a birthday
# add_birthday(birthdays, "Alice", "1990-05-15")

print("Stored Birthdays:", birthdays)
