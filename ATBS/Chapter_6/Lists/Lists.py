# Initialize an empty list to store cat names
cat_names = []

# Start an infinite loop to continuously accept cat name inputs
while True:
    # Prompt the user to enter a cat name, showing the current cat number
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
          ' (Or enter nothing to stop.):')

    # Get user input for the cat name
    name = input()

    # If user enters nothing (empty string), break out of the loop
    if name == '':
        break

    # Add the new cat name to the list using list concatenation
    cat_names = cat_names + [name]  # List concatenation

# Print header before displaying all cat names
print('The cat names are:')

# Loop through each cat name in the list and print it with indentation
for name in cat_names:
    print('  ' + name)