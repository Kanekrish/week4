# Function to calculate the sum of two weights
def sum_weights(person_weight, inventory_weight):
    """Calculates the sum of two weights.

  Args:
    person_weight: The weight of the person.
    inventory_weight: The weight of the inventory.

  Returns:
    The total weight of the person and their inventory.
  """

    total_weight = person_weight + inventory_weight
    return total_weight


# Function to calculate the average weight of two weights
def calc_avg_weight(person_weight, inventory_weight):
    """Calculates the average weight of two weights.

  Args:
    person_weight: The weight of the person.
    inventory_weight: The weight of the inventory.

  Returns:
    The average weight of the person and their inventory.
  """

    total_weight = sum_weights(person_weight, inventory_weight)
    avg_weight = total_weight / 2
    return avg_weight


# Function to run the program and prompt the user for input
def run():
    """Prompts the user to enter the weight of the person and their inventory,
  and then prompts the user to enter either the word "sum" or "average".
  Then, displays the total weight or average weight as appropriate.
  """

    # Prompt the user for the weight of the person and their inventory.
    person_weight = float(input("Enter your weight: "))
    inventory_weight = float(input("Enter the weight of your inventory: "))

    # Prompt the user to enter either the word "sum" or "average".
    weight_type = input("Enter \"sum\" or \"average\": ")

    # Display the total weight or average weight as appropriate.
    if weight_type == "sum":
        total_weight = sum_weights(person_weight, inventory_weight)
        print("The total weight is:", total_weight)
    elif weight_type == "average":
        avg_weight = calc_avg_weight(person_weight, inventory_weight)
        print("The average weight is:", avg_weight)
    else:
        print("Invalid input.")


# Call the run() function to start the program
if __name__ == "__main__":
    run()
