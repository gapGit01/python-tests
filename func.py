pets = {'cat':'kitty', 'dog':'puppy', 'fish':'malu'}


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")



#for i in pets:
#    describe_pet(animal_type = i,pet_name= pets[i])



describe_pet(pet_name='harry', animal_type='hamster')
