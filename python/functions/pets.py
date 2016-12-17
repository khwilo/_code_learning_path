# the default argument should always follow the non-default one
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Positional arguments
#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')

# Keyword arguments
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# default values
describe_pet(pet_name = 'willie')
