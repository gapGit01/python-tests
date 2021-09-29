
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""

    print (f"\nMaking a {str(size)} inch pizza with the following toppings:")

    for i in toppings:
        print("- " + i)
