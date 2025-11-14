# Continuous authentication loop until correct credentials are provided
while True:
    # Prompt for username
    print('Who are you?')
    name = input('> ')

    # Check if username is correct
    if name != 'Panos':
        continue  # Restart loop if username is incorrect

    # If username is correct, prompt for password
    print('Hello, Panos. What is the password? (It is a fish.)')
    password = input('> ')

    # Check if password is correct
    if password == 'swordfish':
        break  # Exit loop if password is correct

# Grant access after successful authentication
print('Access granted.')