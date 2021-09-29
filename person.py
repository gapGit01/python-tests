def build_person (fist_name, last_name, age=''):

    """Return a dictionary of information about person"""

    person = {'first': fist_name, 'last': last_name}

    if age:
        person['age'] = age

    return person

musician = build_person ('snoop', 'dog', age=34)
print(musician)

