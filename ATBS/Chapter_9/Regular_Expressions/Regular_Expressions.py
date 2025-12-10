import re


def is_phone_number(text):
    """
    Validate if a string matches the format: ###-###-####
    using regular expressions.

    Args:
        text (str): String to validate as a phone number

    Returns:
        bool: True if valid format, False otherwise
    """
    # Pattern: 3 digits - 3 digits - 4 digits
    pattern = r'^\d{3}-\d{3}-\d{4}$'

    # Check if text matches the pattern
    return bool(re.match(pattern, text))


# Test cases
print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
print('Is "Moshi moshi" a phone number?', is_phone_number('Moshi moshi'))