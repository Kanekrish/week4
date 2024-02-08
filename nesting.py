def identify():
    # Ask the user to enter a word representing what they see
    sighting = input("Enter a word representing what you see: ")

    # Read the user's response
    if sighting == "a large boulder":
        # If the user's response is "a large boulder" then the message "It's time to run!" should be displayed
        print("It's time to run!")
    else:
        # Otherwise the message "We will be fine." should be displayed
        print("We will be fine.")


# Call the identify function
identify()
