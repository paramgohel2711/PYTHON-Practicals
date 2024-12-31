# Get user input for the color code
s = input("Enter A Color Code (e.g., FFFFFF): ")

# Convert each color component from hexadecimal to decimal
r = int(s[0:2], 16)
g = int(s[2:4], 16)
b = int(s[4:6], 16)

# Display the RGB values
print("RGB Values:", r, g, b)