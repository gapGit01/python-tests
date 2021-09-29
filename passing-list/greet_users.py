def greet_user(names):
    """Print a simple greeting to each user in the list. """

    for name in names:
        msg = f"Hello, {name.title()} !"
        print(msg)

username = ['kallu', 'lk', 'ig']
greet_user(username)
