# Program Started!
print("Program Started!")

# Please enter a standard character:
print("Please enter a standard character:")
letter = input()

# Check that a single letter has been entered
if len(letter) == 1:
    # Determine the ASCII code of the character
    ascii_code = ord(letter)

    # Display the ASCII code
    print("The ASCII code for {} is {}.".format(letter, ascii_code))
else:
    # Display an error message
    print("Please enter a single character.")

# Program Ended!
print("Program Ended!")
