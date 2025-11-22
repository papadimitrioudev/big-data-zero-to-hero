# Set the value of spam variable - change this number to test different cases
spam = 5

# Check if spam is an integer AND less than 10
if isinstance(spam, int) and spam < 10:
    # If both conditions are true, raise an AssertionError with message
    raise AssertionError("spam should not be an integer less than 10")
else:
    # If either condition is false, print success message
    print("No error - spam is OK")