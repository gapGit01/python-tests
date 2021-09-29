def get_formatted_name(fist_name, last_name):

    """Return a full name, neatly formatted"""

    full_name = fist_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('snoop', 'dog')
print(musician)

