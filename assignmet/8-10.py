
def show_magicians(names):

    """Printing a list"""
    for i in names:
        print(i)
        mname.append(i)

def make_greet(mnames):
    for i in mnames:
       print(f"\nThe Great to each magician’s {i}")


"""You can write this way"""
Name=(['hannah', 'ty', 'margot'])
mname = []

show_magicians(Name)
make_greet(mname)
