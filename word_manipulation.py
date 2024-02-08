# Function to display a word in an ASCII art box
def display_in_box(word):
    """Displays a word in an ASCII art box.

  Args:
    word: The word to display.
  """

    print("+" + "-" * len(word) + "+")
    print("|" + word + "|")
    print("+" + "-" * len(word) + "+")


# Function to display a word in lower-case
def display_lower_case(word):
    """Displays a word in lower-case.

  Args:
    word: The word to display.
  """

    print(word.lower())


# Function to display a word in upper-case
def display_upper_case(word):
    """Displays a word in upper-case.

  Args:
    word: The word to display.
  """

    print(word.upper())


# Function to display a word with its mirrored word
def display_mirrored(word):
    """Displays a word with its mirrored word.

  Args:
    word: The word to display.
  """

    print(word + " | " + word[::-1])


# Function to display a word multiple times alternating between upper-case and lower-case
def display_repeat(word, number_of_times):
    """Displays a word multiple times alternating between upper-case and lower-case.

  Args:
    word: The word to display.
    number_of_times: The number of times to display the word.
  """

    for i in range(number_of_times):
        if i % 2 == 0:
            print(word.upper())
        else:
            print(word.lower())


# Function to run the program and prompt the user for input
def run():
    """Prompts the user to enter a word and a choice of how to manipulate it.
  Then, performs the appropriate action and displays the result.
  """

    # Prompt the user to enter a word.
    word = input("Enter a word: ")

    # Prompt the user to choose one of the five options.
    choice = int(input(
        "Choose an option: \n1) Display in a Box \n2) Display Lower-case \n3) Display Upper-case \n4) Display "
        "Mirrored \n5) Repeat \n"))

    # Perform the appropriate action based on the user's choice.
    if choice == 1:
        display_in_box(word)
    elif choice == 2:
        display_lower_case(word)
    elif choice == 3:
        display_upper_case(word)
    elif choice == 4:
        display_mirrored(word)
    elif choice == 5:
        number_of_times = int(input("Enter the number of times to repeat the word: "))
        display_repeat(word, number_of_times)
    else:
        print("Invalid choice.")


# Call the run() function to start the program
if __name__ == "__main__":
    run()
