# Import necessary modules
import os

# Define input file path
input_path = os.path.join(os.getcwd(), "input.md")

# Read HEX code from input file
with open(input_path, "r") as f:
    hex_code = f.read().strip()

# Convert HEX to RGB
red = int(hex_code[:2], 16)
green = int(hex_code[2:4], 16)
blue = int(hex_code[4:], 16)

# Print RGB code
print(f"RGB code: ({red}, {green}, {blue})")
