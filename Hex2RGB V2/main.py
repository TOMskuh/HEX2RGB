def hex_to_rgb(hex_code):
    try:
        hex_code = hex_code.strip('#')
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return r, g, b
    except (ValueError, IndexError):
        return None


# Read HEX code from file
try:
    with open("input.txt", "r") as file:
        hex_value = file.read().strip()
except FileNotFoundError:
    print("File not found.")
    exit(1)

# Convert HEX to RGB
rgb_value = hex_to_rgb(hex_value)

# Check conversion result
if rgb_value is None:
    print("Conversion failed. Please try again.")
else:
    print(f"RGB code: {rgb_value}")
    print("Thank you for using the code.")
