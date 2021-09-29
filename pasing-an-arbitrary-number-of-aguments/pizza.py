
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested. """
    """Summaraize the pizza we are  about to make."""


    print(f"\nMakeing a {str(size)} -inch pizza with the following toppings")

    print ("\nMakeing a pizza we are about to make.")
    for i in toppings:
        print("-" + i)

make_pizza(23, 'pepperoni')
make_pizza(16, 'mushroon', 'green peppers', 'extra cheese')
