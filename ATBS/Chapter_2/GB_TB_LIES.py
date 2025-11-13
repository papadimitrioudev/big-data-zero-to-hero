# Get storage unit type from user
print("Enter unit : GB or TB")
unit = input()

# Calculate the discrepancy between decimal and binary definitions
# For TB: 1 TB (decimal) = 10^12 bytes, 1 TiB (binary) = 2^40 bytes
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776  # 1TB / 1TiB
# For GB: 1 GB (decimal) = 10^9 bytes, 1 GiB (binary) = 2^30 bytes
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824  # 1GB / 1GiB

# Display the calculated discrepancy
print(discrepancy)
