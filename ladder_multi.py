def display_ladder(steps):
    """Displays an ASCII ladder with the given number of steps."""
    for i in range(steps - 1, -1, -1):
        print(" " * i + "|" + " " * (steps - i - 1) + "|")
    print("-" * steps)


def create_ladder():
    """Prompts the user for the number of steps on the ladder and then displays the ladder."""
    steps = int(input("How many steps does the ladder have? "))
    display_ladder(steps)


# Call the create_ladder() function
create_ladder()
