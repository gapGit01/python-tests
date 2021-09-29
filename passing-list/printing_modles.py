unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_desing = unprinted_designs.pop()

    #Simulate creating a 3D print from the design
    print ("Printing modle: " + current_desing)
    completed_models.append(current_desing)    


# Display all completed models.
print("\nThe following models have been printed\n")
for i in completed_models:
    print(i)
