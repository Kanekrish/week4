# Program Started!
print("Program Started!")

# Please enter an ASCII code:
print("Please enter an ASCII code:")

# Read in the user's response
user_input = input()

# Convert the input to a positive integer
ascii_code = abs(int(user_input))

# Check that the number is in the range 32 - 126 (inclusive)
if 32 <= ascii_code <= 126:
    # Determine the ASCII character from the number
    ascii_character = chr(ascii_code)

    # Display the message
    print("The character represented by the ASCII code {} is {}.".format(ascii_code, ascii_character))
else:
    # Display an error message
    print("The ASCII code {} is not in the range 32 - 126 (inclusive). Please enter a valid ASCII code.".format(ascii_code))

# Program Ended!
print("Program Ended!")
