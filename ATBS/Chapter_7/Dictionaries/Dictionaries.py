# Birthday database application
# Stores and retrieves birthday information for contacts

# Dictionary to store name-birthday pairs
birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4'
}

# Main program loop
while True:
    # Prompt user for a name
    print('Enter a name: (blank to quit)')
    name = input()

    # Exit condition - blank input
    if name == '':
        break

    # Check if name exists in database
    if name in birthdays:
        # Display existing birthday information
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        # Handle new entry
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()

        # Add new birthday to database
        birthdays[name] = bday
        print('Birthday database updated.')