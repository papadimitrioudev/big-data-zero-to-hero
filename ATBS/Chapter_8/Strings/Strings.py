# Main program loop for user input validation

# Loop until valid age input is received
while True:
    # Prompt user for age input
    print('Enter your age:')
    age = input()

    # Check if input contains only decimal digits
    if age.isdecimal():
        break  # Exit loop if input is valid

    # Display error message for non-numeric input
    print('Please enter a number for your age.')

# Loop until valid password input is received
while True:
    # Prompt user for password input
    print('Select a new password (letters and numbers only):')
    password = input()

    # Check if input contains only alphanumeric characters
    if password.isalnum():
        break  # Exit loop if input is valid

    # Display error message for invalid password format
    print('Passwords can only have letters and numbers.')